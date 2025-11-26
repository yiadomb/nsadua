# nsadua.com Build Roadmap - Your Step-by-Step Guide

## 🎯 My Role as Your Coach

I'm here to:
- ✅ Guide you through each phase
- ✅ Answer technical questions
- ✅ Review your code and suggest improvements
- ✅ Help debug issues
- ✅ Provide code snippets and templates
- ✅ Clarify WordPress/WooCommerce concepts
- ❌ NOT write all the code for you (you'll learn more this way!)

---

## 📋 Build Phases Overview

### Phase 1: Foundation & Setup
**Goal**: Get WordPress running with WooCommerce and basic structure

### Phase 2: Product Catalog
**Goal**: Create sash products and set up the catalog

### Phase 3: Customization System
**Goal**: Build the form-based customization on product pages

### Phase 4: Entry Paths
**Goal**: Create Homepage, Gallery, and Customise landing page

### Phase 5: Logo & Auto-Population Logic
**Goal**: Implement school/department matching and logo assignment

### Phase 6: Checkout & Orders
**Goal**: Customize checkout and store customization data

### Phase 7: Polish & Launch
**Goal**: Mobile optimization, testing, and launch prep

---

## 🗺️ Detailed Phase Breakdown

### **PHASE 1: Foundation & Setup** ⏱️ ~2-3 days

#### Step 1.1: WordPress Setup
- [ ] Set up WordPress.com Business account (or self-hosted)
- [ ] Install required plugins:
  - [ ] WooCommerce
  - [ ] Elementor Pro
  - [ ] WP Offload Media (if using S3) - optional
- [ ] Choose/install a lightweight theme (Astra, GeneratePress, or custom)
- [ ] Configure basic WordPress settings

**Coach Questions to Ask:**
- "What's your hosting situation? WordPress.com Business or self-hosted?"
- "Do you have Elementor Pro license?"
- "Want to use S3 for assets or WordPress Media Library?"

#### Step 1.2: Custom Plugin Structure
- [ ] Create custom plugin folder: `nsadua-custom/`
- [ ] Create main plugin file: `nsadua-custom.php`
- [ ] Set up basic plugin structure
- [ ] Activate plugin

**I'll provide:** Plugin template code

#### Step 1.3: Database Tables
- [ ] Create `wp_schools` table
- [ ] Create `wp_departments` table
- [ ] Create `wp_programme_suggestions` table
- [ ] Create `wp_product_school_associations` table (optional)

**I'll provide:** SQL schema and installation code

**Checkpoint:** WordPress running, plugin active, database tables created

---

### **PHASE 2: Product Catalog** ⏱️ ~3-4 days

#### Step 2.1: Create First Sash Product
- [ ] Upload high-quality sash photo to Media Library
- [ ] Create WooCommerce product
- [ ] Set product image
- [ ] Set base price (e.g., 150 GHS)
- [ ] Add product name and description
- [ ] Publish product

**Coach Tip:** Start with 2-3 products to test the flow

#### Step 2.2: Product Categories
- [ ] Create product categories (e.g., "Patriotic", "Academic", "Custom")
- [ ] Create school-specific categories (e.g., "University of Ghana", "KNUST")
- [ ] Assign products to categories

#### Step 2.3: Product Catalog Page
- [ ] Create "Shop" or "Browse Sashes" page in Elementor
- [ ] Add WooCommerce Products widget
- [ ] Configure grid layout (responsive)
- [ ] Test on mobile

**Checkpoint:** Can browse products, see prices, click to product page

---

### **PHASE 3: Customization System** ⏱️ ~4-5 days

#### Step 3.1: Choose Customization Method
**Option A:** WooCommerce Product Add-ons Plugin (easiest)
- [ ] Install plugin (e.g., "WooCommerce Product Add-ons" or "Extra Product Options")
- [ ] Configure add-on fields on product

**Option B:** Custom PHP Fields (more control)
- [ ] Add custom fields using WooCommerce hooks
- [ ] Create form HTML
- [ ] Handle form submission

**I'll help you decide** based on your comfort level

#### Step 3.2: Build Customization Form
- [ ] School dropdown field
- [ ] Department dropdown field (populated based on school)
- [ ] Programme text field
- [ ] Name text field
- [ ] Logo assignment display area (thumbnails)
- [ ] Review section
- [ ] Confirmation checkbox
- [ ] Add to Cart button

**I'll provide:** Code templates for each field type

#### Step 3.3: Form Styling
- [ ] Style form in Elementor
- [ ] Make it mobile-responsive
- [ ] Add validation (required fields)
- [ ] Test form submission

**Checkpoint:** Product page shows form, can fill fields, see logo thumbnails

---

### **PHASE 4: Entry Paths** ⏱️ ~3-4 days

#### Step 4.1: Homepage
- [ ] Create Home page in Elementor
- [ ] Add hero section with mission statement
- [ ] Add 3-4 sash product images
- [ ] Link images to product pages
- [ ] Add "Customise" CTA button
- [ ] Make mobile-responsive

#### Step 4.2: Gallery Page
- [ ] Create Gallery page in Elementor
- [ ] Add gallery widget or image grid
- [ ] Link each image to its product page
- [ ] Add "I Want This Sash" overlay/button (optional)
- [ ] Make mobile-responsive

#### Step 4.3: Customise Landing Page
- [ ] Create Customise page
- [ ] Build onboarding form:
  - [ ] Occasion field
  - [ ] School field
  - [ ] Programme field
  - [ ] Department field
  - [ ] Name field
- [ ] Add submit button
- [ ] Handle form submission → redirect to filtered product catalog

**I'll provide:** Form handling code and redirect logic

#### Step 4.4: Product Filtering
- [ ] Create filtered product catalog page
- [ ] Read URL parameters (school, department, etc.)
- [ ] Filter WooCommerce products by school category
- [ ] Display filtered results
- [ ] Pre-fill product form when user selects a sash

**I'll provide:** Filtering code using WooCommerce hooks

**Checkpoint:** Both entry paths work, users can navigate to products

---

### **PHASE 5: Logo & Auto-Population Logic** ⏱️ ~5-6 days

#### Step 5.1: Logo Management System
- [ ] Create admin interface for managing schools
- [ ] Create admin interface for managing departments
- [ ] Upload school logos
- [ ] Upload department logos
- [ ] Link logos to schools/departments in database

**I'll provide:** Admin panel code template

#### Step 5.2: Logo Auto-Assignment API
- [ ] Create WordPress REST API endpoint: `/wp-json/nsadua/v1/get-logos`
- [ ] Endpoint accepts: school_id, department_id
- [ ] Endpoint returns: left_logo_url, right_logo_url
- [ ] Handle cases where logos don't exist (fallback)

**I'll provide:** REST API endpoint template

#### Step 5.3: Frontend Logo Assignment
- [ ] Add JavaScript to product page
- [ ] Listen for School + Department selection
- [ ] Make AJAX call to logo API
- [ ] Display logo thumbnails in form
- [ ] Store logo URLs for order

**I'll provide:** JavaScript code template

#### Step 5.4: Programme Auto-Complete
- [ ] Populate `wp_programme_suggestions` table with sample data
- [ ] Create REST API endpoint for programme suggestions
- [ ] Add autocomplete JavaScript to programme field
- [ ] Filter suggestions by school/department

**I'll provide:** Autocomplete implementation

**Checkpoint:** Selecting school/department shows correct logos, programme autocomplete works

---

### **PHASE 6: Checkout & Orders** ⏱️ ~3-4 days

#### Step 6.1: Store Customization in Cart
- [ ] Use WooCommerce hooks to save form data to cart item
- [ ] Store: school, department, programme, name, logo URLs
- [ ] Display customization summary in cart

**I'll provide:** Cart customization code

#### Step 6.2: Shipping Setup
- [ ] Configure WooCommerce shipping zones
- [ ] Add "Standard" shipping method (20 GHS)
- [ ] Add "Express" shipping method (35 GHS)
- [ ] Test shipping calculation

#### Step 6.3: Checkout Customization
- [ ] Ensure customization data shows in checkout
- [ ] Customize checkout page in Elementor (if needed)
- [ ] Test checkout flow

#### Step 6.4: Order Storage
- [ ] Use WooCommerce hooks to save customization to order meta
- [ ] Display customization in admin order view
- [ ] Display customization in customer order confirmation email

**I'll provide:** Order meta storage code

#### Step 6.5: Thank You Page
- [ ] Customize WooCommerce Thank You page
- [ ] Show order number
- [ ] Show estimated delivery time
- [ ] Add Elementor customization if needed

**Checkpoint:** Complete order flow works, customization saved to orders

---

### **PHASE 7: Polish & Launch** ⏱️ ~3-5 days

#### Step 7.1: Mobile Optimization
- [ ] Test all pages on mobile devices
- [ ] Fix responsive issues
- [ ] Optimize form for touch
- [ ] Test product images on mobile

#### Step 7.2: Content Pages
- [ ] Create About Us page
- [ ] Create Contact page with form
- [ ] Create FAQ page (collapsible sections)
- [ ] Create Terms & Privacy pages
- [ ] Create friendly 404 page

#### Step 7.3: Testing
- [ ] Test complete user flow (both entry paths)
- [ ] Test logo assignment for multiple schools
- [ ] Test programme autocomplete
- [ ] Test checkout with different shipping options
- [ ] Test order confirmation emails
- [ ] Test on different browsers
- [ ] Test on different devices

#### Step 7.4: Performance
- [ ] Optimize images (compress, WebP if possible)
- [ ] Enable caching (if self-hosted)
- [ ] Test page load speeds
- [ ] Fix any slow queries

#### Step 7.5: Launch Prep
- [ ] Set up Google Analytics
- [ ] Set up payment gateway (Stripe, PayPal, etc.)
- [ ] Test payment processing
- [ ] Set up email notifications
- [ ] Create admin documentation
- [ ] Backup site

**Checkpoint:** Site is polished, tested, and ready for launch!

---

## 🎓 How We'll Work Together

### When You're Stuck:
1. **Ask me specific questions** - "How do I filter WooCommerce products by category?"
2. **Share your code** - I'll review and suggest improvements
3. **Describe the problem** - "The logo isn't showing when I select a school"
4. **Ask for code snippets** - "Can you show me how to create a REST API endpoint?"

### What I'll Provide:
- ✅ Code templates and snippets
- ✅ Step-by-step instructions
- ✅ WordPress/WooCommerce explanations
- ✅ Debugging help
- ✅ Architecture guidance
- ✅ Best practices

### What You'll Do:
- ✅ Write the code (with my guidance)
- ✅ Test everything
- ✅ Make design decisions
- ✅ Upload content
- ✅ Build pages in Elementor

---

## 📚 Resources I'll Create for You

1. **Code Templates Folder** - Reusable code snippets
2. **Technical Guides** - Detailed explanations
3. **Database Schema** - Complete SQL structure
4. **API Documentation** - Endpoint specifications
5. **Troubleshooting Guide** - Common issues and solutions

---

## 🚀 Let's Start!

**Your first task:** Tell me which phase you want to start with, or if you need help with the initial setup (hosting, WordPress installation, etc.)

I'm ready to coach you through this! 💪
