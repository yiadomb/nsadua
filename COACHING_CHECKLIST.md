# nsadua.com Build Checklist

Use this checklist to track your progress. Check off items as you complete them!

## Phase 1: Foundation & Setup

### WordPress Setup
- [ ] WordPress installed (WordPress.com Business or self-hosted)
- [ ] WooCommerce plugin installed and activated
- [ ] Elementor Pro installed and activated
- [ ] Theme chosen and installed
- [ ] Basic WordPress settings configured

### Custom Plugin
- [ ] Plugin folder created: `nsadua-custom/`
- [ ] Main plugin file created: `nsadua-custom.php`
- [ ] Plugin activated
- [ ] Basic plugin structure working

### Database
- [ ] `wp_schools` table created
- [ ] `wp_departments` table created
- [ ] `wp_programme_suggestions` table created
- [ ] `wp_product_school_associations` table created (optional)

---

## Phase 2: Product Catalog

### Products
- [ ] First sash product created
- [ ] Product image uploaded
- [ ] Product price set
- [ ] Product published
- [ ] 3-5 test products created

### Categories
- [ ] Product categories created (Patriotic, Academic, etc.)
- [ ] School-specific categories created
- [ ] Products assigned to categories

### Catalog Page
- [ ] Product catalog page created in Elementor
- [ ] WooCommerce Products widget added
- [ ] Grid layout configured
- [ ] Mobile responsive tested

---

## Phase 3: Customization System

### Customization Method Chosen
- [ ] Decided: Product Add-ons plugin OR custom PHP
- [ ] Plugin installed (if using plugin method)
- [ ] Custom fields code written (if using custom method)

### Form Fields
- [ ] School dropdown field
- [ ] Department dropdown (populated by school)
- [ ] Programme text field
- [ ] Name text field
- [ ] Logo display area
- [ ] Review section
- [ ] Confirmation checkbox
- [ ] Add to Cart button

### Form Functionality
- [ ] Form displays on product page
- [ ] Fields are required/validated
- [ ] Form is mobile-responsive
- [ ] Form styling complete

---

## Phase 4: Entry Paths

### Homepage
- [ ] Home page created in Elementor
- [ ] Hero section with mission
- [ ] 3-4 sash product images added
- [ ] Images linked to product pages
- [ ] "Customise" CTA button added
- [ ] Mobile responsive

### Gallery Page
- [ ] Gallery page created
- [ ] Sash images displayed
- [ ] Images linked to product pages
- [ ] "I Want This Sash" buttons (optional)
- [ ] Mobile responsive

### Customise Landing Page
- [ ] Customise page created
- [ ] Onboarding form built:
  - [ ] Occasion field
  - [ ] School field
  - [ ] Programme field
  - [ ] Department field
  - [ ] Name field
- [ ] Form submission handler
- [ ] Redirect to filtered catalog working

### Product Filtering
- [ ] Filtered catalog page created
- [ ] URL parameter reading works
- [ ] Product filtering by school works
- [ ] Pre-filling product form works

---

## Phase 5: Logo & Auto-Population

### Logo Management
- [ ] Admin interface for schools created
- [ ] Admin interface for departments created
- [ ] School logos uploaded
- [ ] Department logos uploaded
- [ ] Logos linked in database

### Logo API
- [ ] REST API endpoint created: `/wp-json/nsadua/v1/get-logos`
- [ ] Endpoint accepts school_id and department_id
- [ ] Endpoint returns logo URLs
- [ ] Fallback handling for missing logos

### Frontend Logo Assignment
- [ ] JavaScript listens for school/department selection
- [ ] AJAX call to logo API works
- [ ] Logo thumbnails display in form
- [ ] Logo URLs stored for order

### Programme Auto-Complete
- [ ] Programme suggestions table populated
- [ ] REST API endpoint for suggestions created
- [ ] Autocomplete JavaScript added
- [ ] Filtering by school/department works

---

## Phase 6: Checkout & Orders

### Cart Customization
- [ ] Customization data saved to cart item
- [ ] Customization summary shows in cart
- [ ] All fields stored correctly

### Shipping
- [ ] Shipping zones configured
- [ ] Standard shipping (20 GHS) added
- [ ] Express shipping (35 GHS) added
- [ ] Shipping calculation tested

### Checkout
- [ ] Customization data shows in checkout
- [ ] Checkout page customized (if needed)
- [ ] Checkout flow tested

### Order Storage
- [ ] Customization saved to order meta
- [ ] Customization shows in admin order view
- [ ] Customization shows in order email

### Thank You Page
- [ ] Thank You page customized
- [ ] Order number displayed
- [ ] Delivery ETA displayed

---

## Phase 7: Polish & Launch

### Mobile Optimization
- [ ] All pages tested on mobile
- [ ] Responsive issues fixed
- [ ] Forms optimized for touch
- [ ] Images optimized for mobile

### Content Pages
- [ ] About Us page created
- [ ] Contact page with form created
- [ ] FAQ page created (collapsible)
- [ ] Terms page created
- [ ] Privacy page created
- [ ] 404 page created

### Testing
- [ ] Complete user flow tested (Path 1)
- [ ] Complete user flow tested (Path 2)
- [ ] Logo assignment tested (multiple schools)
- [ ] Programme autocomplete tested
- [ ] Checkout tested (both shipping options)
- [ ] Order emails tested
- [ ] Cross-browser testing done
- [ ] Cross-device testing done

### Performance
- [ ] Images optimized
- [ ] Caching enabled (if applicable)
- [ ] Page load speeds acceptable
- [ ] Slow queries fixed

### Launch Prep
- [ ] Google Analytics set up
- [ ] Payment gateway configured
- [ ] Payment processing tested
- [ ] Email notifications working
- [ ] Admin documentation created
- [ ] Site backed up

---

## 🎉 Launch Ready!

- [ ] All checkboxes above completed
- [ ] Final review done
- [ ] Ready to go live!

---

**Last Updated:** [Date]
**Current Phase:** [Phase Number]
**Next Steps:** [What you're working on]
