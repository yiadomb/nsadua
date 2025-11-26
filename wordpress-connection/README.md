# WordPress.com & Elementor Pro Connection Guide

This directory contains tools to connect to your WordPress.com site and Elementor Pro so I can track progress and understand your current site state.

## 🔐 Setting Up API Access

### Step 1: WordPress.com Application Password

1. Go to your WordPress.com site
2. Navigate to **Users > Profile** (or **Users > Your Profile**)
3. Scroll down to **Application Passwords**
4. Create a new application password:
   - Name it: "Cursor AI Assistant" or "Development Tools"
   - Click **Add New Application Password**
   - **Copy the password immediately** (you won't see it again!)
5. You'll get a password like: `xxxx xxxx xxxx xxxx xxxx xxxx`

### Step 2: WooCommerce REST API (Optional but Recommended)

1. Go to **WooCommerce > Settings > Advanced > REST API**
2. Click **Add Key**
3. Fill in:
   - **Description**: "Cursor AI Assistant"
   - **User**: Select your admin user
   - **Permissions**: Read/Write (or Read if you only want me to view)
4. Click **Generate API Key**
5. **Copy both the Consumer Key and Consumer Secret**

### Step 3: Configure Connection

1. Copy `config.example.json` to `config.json`:
   ```bash
   cp wordpress-connection/config.example.json wordpress-connection/config.json
   ```

2. Edit `config.json` with your credentials:
   ```json
   {
     "wordpress": {
       "site_url": "https://nsadua.wordpress.com",
       "api_url": "https://nsadua.wordpress.com/wp-json/wp/v2",
       "application_password": {
         "username": "your-wordpress-username",
         "password": "xxxx xxxx xxxx xxxx xxxx xxxx"
       }
     },
     "woocommerce": {
       "api_url": "https://nsadua.wordpress.com/wp-json/wc/v3",
       "consumer_key": "ck_abc123...",
       "consumer_secret": "cs_xyz789..."
     }
   }
   ```

3. **Important**: Add `config.json` to `.gitignore` to keep credentials safe!

## 📊 What I Can Access

Once configured, I can:

### WordPress REST API
- ✅ Read all pages and posts
- ✅ Read page content and metadata
- ✅ Read Elementor data (stored in post meta)
- ✅ Read media library items
- ✅ Read categories and tags

### WooCommerce REST API
- ✅ Read all products
- ✅ Read product details, prices, images
- ✅ Read orders (if permissions allow)
- ✅ Read product categories

### Elementor Data
- ✅ Read Elementor page builder data (via post meta)
- ✅ Understand page structure and widgets used
- ✅ Track which pages are built with Elementor

## 🚀 Using the Connection

### Fetch Current Site State

Run the connection script to see what's currently on your site:

```bash
python wordpress-connection/fetch_site_state.py
```

This will show:
- All pages and their status
- All products and their details
- Elementor-built pages
- Current progress against the roadmap

### I Can Also:

1. **Check Progress**: I can query your site to see what's been built
2. **Understand Context**: See what pages/products exist before making recommendations
3. **Track Changes**: Compare current state with the roadmap
4. **Provide Specific Help**: Give advice based on your actual site structure

## 🔒 Security Notes

- **Never commit `config.json`** to git
- Application passwords can be revoked anytime
- WooCommerce API keys can be regenerated
- Use Read-only permissions if you only want me to view (not modify)

## ❓ Troubleshooting

### "Authentication failed"
- Check your username and application password
- Make sure there are no extra spaces in the password
- Verify the site URL is correct

### "WooCommerce API not found"
- Make sure WooCommerce is installed and activated
- Check that the REST API is enabled in WooCommerce settings
- Verify the consumer key/secret are correct

### "Cannot access Elementor data"
- Elementor data is stored in post meta
- I can access it via WordPress REST API if the post is accessible
- Make sure the page/post is published or you have proper permissions

## 📝 Next Steps

Once you've set up the connection:

1. Share that you've configured it
2. I'll run a site state check
3. We can start building with full context of what exists!
