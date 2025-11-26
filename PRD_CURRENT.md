# nsadua.com Revised PRD - Standard Interactive Web Flow

## Overview

This revised product requirements document outlines the strategy for nsadua.com as a high-quality, interactive e-commerce platform. In this iteration, the complex live-preview canvas and Fabric.js editor are removed in favor of a streamlined, form-based customization workflow. The core value proposition remains the same: offering school-specific sashes with accurate logos and details, hosted on WordPress.com Business with Elementor Pro and WooCommerce, supported by a flat-rate pricing engine and a mobile-first design.

---

## Overall Interaction and User Flow

The platform retains two primary entry paths, but the destination is now a sophisticated product configuration form rather than a graphical editor.

### Entry Path 1: Gallery/Homepage → Product Page

- Every sash image displayed on the marketing site is saved in the database as a **product variant**
- When a visitor clicks on a sash image in a gallery or blog post, they are presented with an **"I Want This Sash"** button
- Clicking this button navigates the user directly to a dedicated **Product Detail Page** for that specific sash design
- The static image of the blank sash is displayed prominently as a reference, accompanied by a comprehensive input form

### Entry Path 2: Direct Customise Link

- Users fill out the initial onboarding form specifying their **Occasion, School, Programme, Department, and Name**
- Upon submission, instead of loading a canvas, the site redirects the user to a **filtered results page**—a catalog view showing only the sash designs relevant to their selected school or institution
- Selecting a design from this list brings them to the Product Detail Page with their onboarding information already **pre-filled** into the customization fields

---

## The Customization Interface

### Product Detail Page Structure

The Product Detail Page serves as the replacement for the previous editor. It features:

- **Desktop Layout**: High-resolution static image of the selected sash on one side + smart customization form on the other
- **Mobile Layout**: Static sash image at the top + customization form below

### Form Fields (Mandatory)

1. **School or Institution** (dropdown)
2. **Programme** (text with auto-complete)
3. **Department or College** (dropdown)
4. **Name** (text with placeholder hint)

### Auto-Population Logic (Background)

**Logo Assignment:**
- When a user selects their School and Department from dropdown menus, the system automatically assigns the correct logos to the order data in the background
- Instead of seeing the logos appear on the sash, the form displays:
  - A confirmation message, OR
  - A small static thumbnail of the crests to be used, labeled **"Left Logo"** and **"Right Logo"**
- This ensures the user knows the correct assets have been selected

**Programme Field:**
- Retains the auto-complete functionality
- As the student types, the system suggests standard formats like **"BSc Electrical Engineering 2025"** to ensure consistency

**Name Field:**
- Continues to use placeholder text to guide the user regarding titles
- Example placeholder: "Miss. Rosemond K. Dei"

### Review Section

Since there is **no live visual preview**, a prominent review section is added at the bottom of the form:

- Reiterates the text exactly as entered
- Displays the names of the selected logos
- Requires the user to tick a checkbox confirming the details are correct before adding the item to the cart

---

## Template and Product Management

### Product Catalog (Replaces Template Chooser)

The Template Chooser is reimagined as a standard **WooCommerce product grid**:

- When users browse for other templates, they view a curated grid of high-quality photos of the blank sashes
- Product cards display:
  - Sash thumbnail
  - Name
  - Category
  - Base price
- The filtering logic remains active, allowing users to sort sashes by school colors or categories

### Simplified Admin Workflow

Because the visual constraints of a canvas are no longer needed, the complexity of managing safe areas, normalized coordinates, and logo zones is removed:

- Administrators simply upload high-quality product photos to the WooCommerce gallery
- Link products to the appropriate school categories
- Set base prices
- No complex metadata management required

---

## Pricing and Cost Calculation

The pricing model remains template-driven and flat-rate:

- Each sash product has a **base price** managed within WooCommerce
- The delivery fee logic is handled during the checkout phase or via a shipping plugin, offering **Standard** and **Express** options
- The total cost is calculated by summing the specific sash price and the chosen delivery method
- The product page updates the displayed price if different sash variants have different costs
- The cart and checkout pages provide a clear breakdown of the item price and the shipping fee

---

## Platform and Asset Hosting

### Simplified Technical Stack

The technical stack is simplified by removing the custom React application:

- The site is built entirely on **WordPress.com Business** using **Elementor Pro** for the frontend design and **WooCommerce** for the transactional functionality
- Asset hosting for product images and logos can remain on **AWS S3** with the **WP Offload Media** plugin to ensure fast loading speeds, OR simply use the **WordPress Media Library** if the volume is manageable
- The complexity of fetching signed URLs for a frontend editor is eliminated
- The deployment is straightforward, relying on standard WordPress theme and plugin updates

---

## Page-by-Page Build Checklist

The build roadmap continues to prioritize mobile users.

### 1. Home Page
- Marketing hero
- Calls to action
- Links to the product catalog

### 2. Gallery Page
- Elementor Pro widgets to display sash photos
- Photos link to their respective product pages

### 3. Customise Landing Page
- Contains the onboarding form
- Passes parameters to the product filter via URL queries

### 4. Product Detail Page ⭐ **CORE PAGE**
- Built using the Single Product template in Elementor
- Contains:
  - Static product image
  - Smart input fields (likely using a Product Add-ons plugin or variable product fields)
  - Review section
  - Add to Cart button

### 5. Checkout Page
- Handles payment and shipping selection

### 6. Success Page
- Provides the order confirmation
- Estimated delivery time

### 7. Standard Pages
- **About Us**: Linked in footer
- **Contact**: Form sending to support inbox
- **FAQ**: Mobile collapsible sections
- **Terms & Privacy**: Static template pages
- **404**: Friendly page suggesting Home/Gallery

### Build Order

1. Home
2. Product Catalog setup
3. Product Detail Page configuration
4. Customise landing + onboarding form
5. Checkout
6. Gallery
7. Supporting static content

---

## Key Differences from Original PRD

### Removed
- ❌ React SPA with Fabric.js canvas editor
- ❌ Live preview/real-time visual updates
- ❌ Safe area constraints and normalized coordinates
- ❌ Logo drag-and-drop zones
- ❌ Complex template metadata system
- ❌ CloudFront signed URLs for editor assets
- ❌ Custom React build pipeline

### Retained
- ✅ Two entry paths (Gallery/Homepage + Direct Customise)
- ✅ Auto-population logic (background assignment)
- ✅ School/Department logo matching
- ✅ Programme auto-complete
- ✅ Template/product filtering by school
- ✅ Flat-rate pricing model
- ✅ Mobile-first design
- ✅ WordPress.com Business + Elementor Pro + WooCommerce

### Simplified
- Form-based customization instead of visual editor
- Standard WooCommerce product pages
- Static image previews instead of interactive canvas
- Simpler admin workflow (just upload photos, no metadata)

---

## Success Metrics

- Clear, intuitive form design
- Reliable logo auto-assignment
- High-quality product images
- Smooth onboarding flow
- Trust-building (review section, clear communication)
