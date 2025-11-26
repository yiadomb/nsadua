#!/usr/bin/env python3
"""
WordPress Site State Fetcher

This script connects to your WordPress.com site and Elementor Pro
to fetch current site state and track progress.
"""

import json
import requests
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Base64 encoding for WordPress Application Password auth
import base64


class WordPressConnector:
    """Connects to WordPress.com REST API"""
    
    def __init__(self, config_path: str = "config.json"):
        """Initialize with config file"""
        config_file = Path(__file__).parent / config_path
        
        if not config_file.exists():
            print(f"❌ Config file not found: {config_file}")
            print(f"   Please copy config.example.json to {config_path} and fill in your credentials")
            sys.exit(1)
        
        with open(config_file) as f:
            self.config = json.load(f)
        
        self.wp_config = self.config.get("wordpress", {})
        self.wc_config = self.config.get("woocommerce", {})
        
        # Setup WordPress API auth
        username = self.wp_config.get("application_password", {}).get("username")
        password = self.wp_config.get("application_password", {}).get("password")
        
        if not username or not password:
            print("❌ WordPress credentials not configured")
            sys.exit(1)
        
        # WordPress.com uses Application Password authentication
        credentials = f"{username}:{password}"
        token = base64.b64encode(credentials.encode()).decode()
        self.wp_headers = {
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json"
        }
        
        self.api_url = self.wp_config.get("api_url", "")
        
        # Setup WooCommerce API auth
        if self.wc_config.get("consumer_key") and self.wc_config.get("consumer_secret"):
            self.wc_auth = (
                self.wc_config.get("consumer_key"),
                self.wc_config.get("consumer_secret")
            )
            self.wc_api_url = self.wc_config.get("api_url", "")
        else:
            self.wc_auth = None
            print("⚠️  WooCommerce API not configured (optional)")
    
    def fetch_pages(self) -> List[Dict]:
        """Fetch all pages from WordPress"""
        try:
            url = f"{self.api_url}/pages"
            response = requests.get(url, headers=self.wp_headers, params={"per_page": 100})
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error fetching pages: {e}")
            return []
    
    def fetch_posts(self) -> List[Dict]:
        """Fetch all posts from WordPress"""
        try:
            url = f"{self.api_url}/posts"
            response = requests.get(url, headers=self.wp_headers, params={"per_page": 100})
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error fetching posts: {e}")
            return []
    
    def fetch_products(self) -> List[Dict]:
        """Fetch all WooCommerce products"""
        if not self.wc_auth:
            return []
        
        try:
            url = f"{self.wc_api_url}/products"
            response = requests.get(url, auth=self.wc_auth, params={"per_page": 100})
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Error fetching products: {e}")
            return []
    
    def fetch_elementor_data(self, page_id: int) -> Optional[Dict]:
        """Fetch Elementor data for a specific page"""
        try:
            # Elementor stores data in post meta
            url = f"{self.api_url}/pages/{page_id}"
            response = requests.get(url, headers=self.wp_headers)
            response.raise_for_status()
            page = response.json()
            
            # Check if Elementor is used
            elementor_data = {}
            if "_elementor_data" in page.get("meta", {}):
                elementor_data["has_elementor"] = True
            else:
                elementor_data["has_elementor"] = False
            
            return elementor_data
        except Exception as e:
            return None
    
    def get_site_state(self) -> Dict:
        """Get complete site state"""
        print("🔍 Fetching site state...")
        
        pages = self.fetch_pages()
        posts = self.fetch_posts()
        products = self.fetch_products()
        
        # Check Elementor usage on pages
        elementor_pages = []
        for page in pages[:10]:  # Check first 10 pages
            elementor_data = self.fetch_elementor_data(page.get("id"))
            if elementor_data and elementor_data.get("has_elementor"):
                elementor_pages.append(page.get("title", {}).get("rendered", "Untitled"))
        
        return {
            "pages": pages,
            "posts": posts,
            "products": products,
            "elementor_pages": elementor_pages,
            "stats": {
                "total_pages": len(pages),
                "published_pages": len([p for p in pages if p.get("status") == "publish"]),
                "total_posts": len(posts),
                "total_products": len(products),
                "elementor_pages_count": len(elementor_pages)
            }
        }


def print_site_state(state: Dict):
    """Pretty print site state"""
    stats = state.get("stats", {})
    
    print("\n" + "="*60)
    print("📊 YOUR WORDPRESS SITE STATE")
    print("="*60)
    
    print(f"\n📄 Pages: {stats.get('total_pages')} total, {stats.get('published_pages')} published")
    if state.get("pages"):
        print("\n   Published Pages:")
        for page in state.get("pages", [])[:10]:
            if page.get("status") == "publish":
                title = page.get("title", {}).get("rendered", "Untitled")
                slug = page.get("slug", "")
                print(f"   • {title} ({slug})")
    
    print(f"\n📝 Posts: {stats.get('total_posts')} total")
    
    print(f"\n🛍️  Products: {stats.get('total_products')} total")
    if state.get("products"):
        print("\n   Products:")
        for product in state.get("products", [])[:10]:
            name = product.get("name", "Untitled")
            price = product.get("price", "N/A")
            status = product.get("status", "unknown")
            print(f"   • {name} - {price} GHS ({status})")
    
    print(f"\n🎨 Elementor Pages: {stats.get('elementor_pages_count')} pages built with Elementor")
    if state.get("elementor_pages"):
        print("\n   Elementor-built Pages:")
        for page_title in state.get("elementor_pages", []):
            print(f"   • {page_title}")
    
    print("\n" + "="*60)
    print("\n✅ Site state fetched successfully!")
    print("   I can now understand your site context and help you build effectively.")


def main():
    """Main function"""
    connector = WordPressConnector()
    
    try:
        state = connector.get_site_state()
        print_site_state(state)
        
        # Save state to file for reference
        output_file = Path(__file__).parent / "site_state.json"
        with open(output_file, "w") as f:
            json.dump(state, f, indent=2, default=str)
        print(f"\n💾 Full state saved to: {output_file}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
