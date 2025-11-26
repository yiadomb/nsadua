#!/usr/bin/env python3
"""
Progress Checker - Compares WordPress site state with roadmap checklist

This script checks what's actually built on your WordPress site
and compares it against the COACHING_CHECKLIST.md to show progress.
"""

import json
import requests
import sys
from pathlib import Path
from typing import Dict, List, Set
import re

# Import the connector
from fetch_site_state import WordPressConnector


class ProgressChecker:
    """Checks progress against the roadmap"""
    
    def __init__(self, connector: WordPressConnector):
        self.connector = connector
        self.checklist_path = Path(__file__).parent.parent / "COACHING_CHECKLIST.md"
    
    def load_checklist(self) -> str:
        """Load the checklist markdown file"""
        if not self.checklist_path.exists():
            return ""
        return self.checklist_path.read_text()
    
    def check_phase_1(self, state: Dict) -> Dict:
        """Check Phase 1: Foundation & Setup"""
        results = {
            "wordpress_setup": {},
            "custom_plugin": {},
            "database": {}
        }
        
        # Check if WooCommerce is active (products exist)
        has_products = len(state.get("products", [])) > 0
        results["wordpress_setup"]["woocommerce_active"] = has_products
        
        # Check if pages exist (WordPress is set up)
        has_pages = len(state.get("pages", [])) > 0
        results["wordpress_setup"]["wordpress_installed"] = has_pages
        
        # Check for Elementor pages
        has_elementor = len(state.get("elementor_pages", [])) > 0
        results["wordpress_setup"]["elementor_active"] = has_elementor
        
        return results
    
    def check_phase_2(self, state: Dict) -> Dict:
        """Check Phase 2: Product Catalog"""
        results = {
            "products_created": len(state.get("products", [])),
            "products_published": len([p for p in state.get("products", []) if p.get("status") == "publish"]),
            "has_catalog_page": False  # Would need to check page content
        }
        
        # Check if any products have images
        products_with_images = [p for p in state.get("products", []) if p.get("images")]
        results["products_with_images"] = len(products_with_images)
        
        return results
    
    def check_phase_4(self, state: Dict) -> Dict:
        """Check Phase 4: Entry Paths"""
        results = {
            "homepage_exists": False,
            "gallery_page_exists": False,
            "customise_page_exists": False
        }
        
        pages = state.get("pages", [])
        page_slugs = [p.get("slug", "").lower() for p in pages]
        page_titles = [p.get("title", {}).get("rendered", "").lower() for p in pages]
        
        # Check for homepage
        if "home" in page_slugs or any("home" in title for title in page_titles):
            results["homepage_exists"] = True
        
        # Check for gallery page
        if "gallery" in page_slugs or any("gallery" in title for title in page_titles):
            results["gallery_page_exists"] = True
        
        # Check for customise page
        if "customise" in page_slugs or "customize" in page_slugs or \
           any("custom" in title for title in page_titles):
            results["customise_page_exists"] = True
        
        return results
    
    def check_all_phases(self, state: Dict) -> Dict:
        """Check all phases"""
        return {
            "phase_1": self.check_phase_1(state),
            "phase_2": self.check_phase_2(state),
            "phase_4": self.check_phase_4(state)
        }
    
    def print_progress_report(self, progress: Dict, state: Dict):
        """Print a progress report"""
        print("\n" + "="*60)
        print("📊 PROGRESS REPORT - nsadua.com")
        print("="*60)
        
        # Phase 1
        p1 = progress.get("phase_1", {})
        wp_setup = p1.get("wordpress_setup", {})
        print("\n🔧 Phase 1: Foundation & Setup")
        print(f"   WordPress Installed: {'✅' if wp_setup.get('wordpress_installed') else '❌'}")
        print(f"   WooCommerce Active: {'✅' if wp_setup.get('woocommerce_active') else '❌'}")
        print(f"   Elementor Active: {'✅' if wp_setup.get('elementor_active') else '❌'}")
        
        # Phase 2
        p2 = progress.get("phase_2", {})
        print("\n🛍️  Phase 2: Product Catalog")
        print(f"   Products Created: {p2.get('products_created', 0)}")
        print(f"   Products Published: {p2.get('products_published', 0)}")
        print(f"   Products with Images: {p2.get('products_with_images', 0)}")
        
        # Phase 4
        p4 = progress.get("phase_4", {})
        print("\n🚪 Phase 4: Entry Paths")
        print(f"   Homepage: {'✅' if p4.get('homepage_exists') else '❌'}")
        print(f"   Gallery Page: {'✅' if p4.get('gallery_page_exists') else '❌'}")
        print(f"   Customise Page: {'✅' if p4.get('customise_page_exists') else '❌'}")
        
        # Overall stats
        stats = state.get("stats", {})
        print("\n📈 Overall Stats")
        print(f"   Total Pages: {stats.get('total_pages', 0)}")
        print(f"   Published Pages: {stats.get('published_pages', 0)}")
        print(f"   Total Products: {stats.get('total_products', 0)}")
        print(f"   Elementor Pages: {stats.get('elementor_pages_count', 0)}")
        
        print("\n" + "="*60)
        print("\n💡 Next Steps:")
        
        # Suggest next steps based on progress
        if not wp_setup.get("wordpress_installed"):
            print("   → Set up WordPress and install required plugins")
        elif not wp_setup.get("woocommerce_active"):
            print("   → Install and activate WooCommerce")
        elif p2.get("products_created", 0) == 0:
            print("   → Create your first sash product")
        elif p2.get("products_created", 0) < 3:
            print("   → Create 2-3 more test products")
        elif not p4.get("homepage_exists"):
            print("   → Build the homepage in Elementor")
        elif not p4.get("gallery_page_exists"):
            print("   → Create the gallery page")
        else:
            print("   → Continue with Phase 3: Customization System")
        
        print()


def main():
    """Main function"""
    try:
        connector = WordPressConnector()
        state = connector.get_site_state()
        
        checker = ProgressChecker(connector)
        progress = checker.check_all_phases(state)
        
        checker.print_progress_report(progress, state)
        
        # Save progress to file
        output_file = Path(__file__).parent / "progress_report.json"
        with open(output_file, "w") as f:
            json.dump({
                "progress": progress,
                "state": state,
                "timestamp": str(Path(__file__).stat().st_mtime)
            }, f, indent=2, default=str)
        print(f"💾 Progress report saved to: {output_file}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
