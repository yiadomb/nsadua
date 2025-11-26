# PRD Analysis: nsadua.com Revised (Simplified Version)

## My Understanding of the Revised System

### Core Concept
A **simplified WordPress e-commerce platform** where students customize graduation sashes through a **form-based interface** instead of a live canvas editor. The platform still delivers school-specific sashes with accurate logos and details, but removes the complexity of real-time visual editing in favor of a streamlined WooCommerce product configuration workflow.

### Key Changes from Original PRD

**REMOVED:**
- ❌ React SPA with Fabric.js canvas editor
- ❌ Live preview/real-time visual updates
- ❌ Safe area constraints and normalized coordinates
- ❌ Logo drag-and-drop zones
- ❌ Complex template metadata system
- ❌ CloudFront signed URLs for editor assets
- ❌ Custom React build pipeline

**RETAINED:**
- ✅ Two entry paths (Gallery/Homepage + Direct Customise)
- ✅ Auto-population logic (background assignment)
- ✅ School/Department logo matching
- ✅ Programme auto-complete
- ✅ Template/product filtering by school
- ✅ Flat-rate pricing model
- ✅ Mobile-first design
- ✅ WordPress.com Business + Elementor Pro + WooCommerce

**SIMPLIFIED:**
- Form-based customization instead of visual editor
- Standard WooCommerce product pages
- Static image previews instead of interactive canvas
- Simpler admin workflow (just upload photos, no metadata)

---

## Architecture Overview

### Platform Stack
- **CMS/Pages**: WordPress.com Business + Elementor Pro
- **E-commerce**: WooCommerce (standard product pages)
- **Customization**: Product Add-ons plugin OR WooCommerce variable products
- **Assets**: WordPress Media Library OR AWS S3 (simplified, no signed URLs needed)
- **No Custom React App**: Pure WordPress solution

### Two Entry Paths (Simplified)

**Path A: Gallery/Homepage → Product Page**
- User clicks sash image (gallery, homepage, blog)
- Each image is a **WooCommerce product variant**
- "I Want This Sash" button → navigates to **Product Detail Page**
- Static image of blank sash displayed
- Comprehensive input form alongside image

**Path B: Direct Customisation**
- User clicks "Customise" link
- Onboarding form: Occasion, School, Programme, Department, Name
- Submit → redirects to **filtered product catalog** (sashes relevant to their school)
- Select design → Product Detail Page with **pre-filled form fields**

---

## The Customization Interface

### Product Detail Page Structure

**Layout:**
- **Desktop**: Static sash image (left) + Customization form (right)
- **Mobile**: Static sash image (top) + Customization form (bottom)

**Form Fields (Mandatory):**
1. **School/Institution** (dropdown)
2. **Programme** (text with auto-complete)
3. **Department/College** (dropdown)
4. **Name** (text with placeholder hint)

### Auto-Population Logic (Background)

**Logo Assignment:**
- When School + Department selected → system **automatically assigns logos** in background
- **No visual canvas update** - instead shows:
  - Confirmation message: "Logos assigned successfully"
  - OR static thumbnails labeled "Left Logo" and "Right Logo"
  - Shows crest images to confirm correct assets selected

**Programme Field:**
- Auto-complete dropdown as user types
- Suggests: "BSc Electrical Engineering 2025"
- Ensures consistency

**Name Field:**
- Placeholder: "Miss. Rosemond K. Dei"
- Helper text about optional titles

### Review Section

Since there's **no live preview**, a prominent review section at bottom:
- Displays all entered text exactly as entered
- Shows names of selected logos
- **Checkbox**: "I confirm these details are correct"
- Required before "Add to Cart"

---

## Template and Product Management

### Product Catalog (Replaces Template Chooser)

**Structure:**
- Standard **WooCommerce product grid**
- High-quality photos of blank sashes
- Product cards show:
  - Thumbnail
  - Name
  - Category
  - Base price

**Filtering:**
- Filter by school colors
- Filter by categories
- Filter by school/institution (from onboarding)

**Admin Workflow (Simplified):**
- Upload high-quality product photos to WooCommerce gallery
- Link products to school categories
- Set base prices
- **No complex metadata** (no safe areas, coordinates, logo zones)

---

## Pricing and Cost Calculation

**Model:**
- **Base Price**: Managed in WooCommerce product settings
- **Delivery Fee**: Standard (20 GHS) or Express (35 GHS)
  - Handled via WooCommerce shipping methods
  - OR shipping plugin
- **Total**: Base price + shipping fee
- Displayed on product page, cart, and checkout

**Calculation:**
- Product page shows base price
- Cart shows item price + shipping
- Checkout shows full breakdown

---

## Platform and Asset Hosting

### Simplified Technical Stack

**No Custom React App:**
- Pure WordPress solution
- Elementor Pro for frontend design
- WooCommerce for e-commerce
- Product Add-ons plugin for customization fields

**Asset Hosting Options:**
- **Option A**: WordPress Media Library (if volume manageable)
- **Option B**: AWS S3 + WP Offload Media (for performance)
- **No signed URLs needed** (no React editor fetching assets)

**Deployment:**
- Standard WordPress theme/plugin updates
- No custom build pipeline
- No React bundle versioning

---

## Page-by-Page Build Checklist

### Mobile-First Priority

1. **Home Page**
   - Marketing hero
   - Call to action → product catalog
   - Sash images linking to product pages

2. **Gallery Page**
   - Elementor Pro gallery widget
   - Sash photos → link to respective product pages
   - "I Want This Sash" buttons

3. **Customise Landing Page**
   - Onboarding form (Occasion, School, Programme, Department, Name)
   - Submit → redirects to filtered product catalog
   - Passes parameters via URL queries

4. **Product Catalog Page**
   - WooCommerce product grid
   - Filtered by school (from onboarding)
   - Filter by category/colors
   - Product cards with thumbnails, name, price

5. **Product Detail Page** ⭐ **CORE PAGE**
   - Static product image (high-res)
   - Smart customization form:
     - School dropdown
     - Programme (auto-complete)
     - Department dropdown
     - Name field
   - Logo assignment confirmation/thumbnails
   - Review section (text summary + logo names + confirmation checkbox)
   - Add to Cart button

6. **Checkout Page**
   - Standard WooCommerce checkout
   - Shipping selection (Standard/Express)
   - Payment processing
   - Price breakdown

7. **Success/Thank You Page**
   - Order confirmation
   - Order number
   - Estimated delivery time

8. **Supporting Pages**
   - About Us
   - Contact (form → support inbox)
   - FAQ (mobile collapsible sections)
   - Terms & Privacy (static templates)
   - 404 (friendly, suggests Home/Gallery)

### Build Order
1. Home
2. Product Catalog setup (WooCommerce products)
3. Product Detail Page configuration
4. Customise landing + onboarding form
5. Checkout
6. Gallery
7. Supporting static content

---

## Feasibility Assessment

### ✅ **Highly Feasible - Much Simpler!**

This revised approach is **significantly more feasible** because:

1. **No React Complexity**: Pure WordPress solution
2. **Standard WooCommerce**: Leverages existing e-commerce platform
3. **Simpler Admin**: Just upload photos, no complex metadata
4. **Easier Deployment**: Standard WordPress updates
5. **Better Performance**: No heavy JavaScript canvas rendering
6. **Lower Maintenance**: Fewer moving parts

### Technical Considerations

#### 1. **Product Customization Fields**

**Option A: WooCommerce Product Add-ons Plugin**
- Plugins like "WooCommerce Product Add-ons" or "Extra Product Options"
- Allows custom fields on product page
- Stores data in order meta
- **Pros**: Easy setup, well-supported
- **Cons**: May need premium plugin

**Option B: Custom WooCommerce Fields**
- Custom PHP code using WooCommerce hooks
- `woocommerce_product_options_general_product_data`
- Store in product meta
- **Pros**: Full control, no plugin cost
- **Cons**: Requires custom development

**Option C: Variable Products**
- Use WooCommerce product variations
- Each combination = variation
- **Pros**: Native WooCommerce
- **Cons**: Can get complex with many options

**Recommendation**: **Option A** (Product Add-ons plugin) for fastest implementation, or **Option B** (custom fields) for full control.

#### 2. **Logo Auto-Assignment Logic**

**Database Structure:**
```sql
wp_schools (id, name, logo_url)
wp_departments (id, school_id, name, logo_url)
wp_product_logo_assignments (product_id, school_id, department_id, left_logo_url, right_logo_url)
```

**Logic Flow:**
1. User selects School + Department from dropdowns
2. JavaScript/AJAX call to WordPress REST API
3. Backend matches School + Department → finds logos
4. Returns logo URLs
5. Display thumbnails in form
6. Store logo URLs in order meta when "Add to Cart"

**Implementation:**
- Custom WordPress REST API endpoint: `/wp-json/nsadua/v1/get-logos`
- AJAX handler in theme/plugin
- Store in `$_POST` or session, then in order meta

#### 3. **Programme Auto-Complete**

**Options:**
- **Option A**: WordPress REST API endpoint with programme suggestions
- **Option B**: Static JavaScript array (if list is small)
- **Option C**: Third-party autocomplete library (Select2, Choices.js)

**Recommendation**: **Option A** (REST API) for dynamic, database-driven suggestions.

**Database:**
```sql
wp_programme_suggestions (id, programme_name, school_id, department_id)
```

#### 4. **Onboarding Form → Product Filter**

**Flow:**
1. User fills onboarding form
2. Submit → `wp_redirect()` to product catalog
3. Pass parameters: `?school=123&department=456&occasion=graduation`
4. WooCommerce query filter: `pre_get_posts` hook
5. Filter products by school category

**Implementation:**
```php
// In functions.php or plugin
add_action('pre_get_posts', 'filter_sash_products_by_school');
function filter_sash_products_by_school($query) {
    if (isset($_GET['school']) && !is_admin()) {
        $school_id = intval($_GET['school']);
        $query->set('tax_query', array(
            array(
                'taxonomy' => 'product_cat',
                'field' => 'term_id',
                'terms' => $school_id
            )
        ));
    }
}
```

#### 5. **Pre-filling Form Fields**

**Method:**
- Store onboarding data in URL parameters
- JavaScript reads URL params on product page load
- Populate form fields via JavaScript
- OR use PHP to pre-populate if using server-side rendering

**Example:**
```
/product/sash-design/?school=university-of-ghana&department=engineering&name=John+Doe
```

#### 6. **Review Section Display**

**Implementation:**
- JavaScript reads all form field values
- Displays in review section div
- Shows logo names/thumbnails (from auto-assignment)
- Requires checkbox check before enabling "Add to Cart"

**Code Structure:**
```javascript
function updateReviewSection() {
    const school = document.getElementById('school').value;
    const programme = document.getElementById('programme').value;
    const department = document.getElementById('department').value;
    const name = document.getElementById('name').value;
    const leftLogo = document.getElementById('left-logo-name').textContent;
    const rightLogo = document.getElementById('right-logo-name').textContent;
    
    // Update review section HTML
    // Enable/disable Add to Cart based on checkbox
}
```

#### 7. **Storing Customization Data in Order**

**WooCommerce Hooks:**
```php
// Save custom fields to order
add_action('woocommerce_checkout_create_order_line_item', 'save_sash_customization', 10, 4);
function save_sash_customization($item, $cart_item_key, $values, $order) {
    if (isset($values['sash_school'])) {
        $item->add_meta_data('School', $values['sash_school']);
        $item->add_meta_data('Department', $values['sash_department']);
        $item->add_meta_data('Programme', $values['sash_programme']);
        $item->add_meta_data('Name', $values['sash_name']);
        $item->add_meta_data('Left Logo', $values['sash_left_logo']);
        $item->add_meta_data('Right Logo', $values['sash_right_logo']);
    }
}
```

---

## Database Schema (Simplified)

```sql
-- Schools
CREATE TABLE wp_schools (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    logo_url VARCHAR(500),
    created_at TIMESTAMP
);

-- Departments
CREATE TABLE wp_departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    school_id INT,
    name VARCHAR(255),
    logo_url VARCHAR(500),
    FOREIGN KEY (school_id) REFERENCES wp_schools(id),
    created_at TIMESTAMP
);

-- Programme Suggestions
CREATE TABLE wp_programme_suggestions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    programme_name VARCHAR(255),
    school_id INT,
    department_id INT,
    FOREIGN KEY (school_id) REFERENCES wp_schools(id),
    FOREIGN KEY (department_id) REFERENCES wp_departments(id),
    created_at TIMESTAMP
);

-- Product-School Associations (for filtering)
CREATE TABLE wp_product_school_associations (
    product_id BIGINT,
    school_id INT,
    priority INT,
    FOREIGN KEY (product_id) REFERENCES wp_posts(ID),
    FOREIGN KEY (school_id) REFERENCES wp_schools(id)
);

-- Logo Assignments (optional, if logos vary by product)
CREATE TABLE wp_product_logo_assignments (
    product_id BIGINT,
    school_id INT,
    department_id INT,
    left_logo_url VARCHAR(500),
    right_logo_url VARCHAR(500),
    FOREIGN KEY (product_id) REFERENCES wp_posts(ID),
    FOREIGN KEY (school_id) REFERENCES wp_schools(id),
    FOREIGN KEY (department_id) REFERENCES wp_departments(id)
);
```

**Note**: Customization data (school, department, programme, name, logos) is stored in WooCommerce order meta, not separate tables.

---

## Implementation Recommendations

### Phase 1: Foundation
1. WordPress setup + WooCommerce configuration
2. Custom plugin structure for logo logic
3. Database tables (schools, departments, programmes)
4. Basic product catalog setup

### Phase 2: Product Pages
1. Product Detail Page template (Elementor)
2. Customization form fields (Product Add-ons or custom)
3. Logo auto-assignment logic (REST API endpoint)
4. Programme auto-complete
5. Review section

### Phase 3: Entry Paths
1. Homepage with product links
2. Gallery page (Elementor)
3. Customise landing page + onboarding form
4. Product filtering by school
5. Pre-filling form from URL params

### Phase 4: Checkout & Orders
1. Store customization in order meta
2. Checkout page customization
3. Order confirmation with details
4. Admin order view (show customization)

### Phase 5: Polish
1. Mobile optimization
2. Error handling
3. Admin interface for managing schools/departments/logos
4. Testing

---

## Advantages of This Approach

1. **Faster Development**: No React build pipeline
2. **Easier Maintenance**: Standard WordPress
3. **Better Performance**: No heavy JavaScript
4. **Lower Cost**: Fewer dependencies
5. **Easier Updates**: Standard WordPress updates
6. **Better SEO**: Server-rendered pages
7. **Mobile-Friendly**: Forms work well on mobile
8. **Accessible**: Standard HTML forms

## Potential Limitations

1. **No Visual Preview**: Users can't see final result before ordering
   - **Mitigation**: High-quality product images, clear review section, trust-building

2. **Less Interactive**: Form-based vs. visual editor
   - **Mitigation**: This is intentional simplification for MVP

3. **Logo Confirmation**: Static thumbnails instead of live preview
   - **Mitigation**: Clear labeling, confirmation checkbox

---

## Conclusion

**Feasibility**: ✅ **Very High - Much Simpler Implementation**

This revised PRD is **significantly more achievable** and can be built faster. It removes the most complex components (React/Fabric.js) while retaining the core value proposition (school-specific sashes with accurate details).

**Key Success Factors:**
1. Clear, intuitive form design
2. Reliable logo auto-assignment
3. Good product images
4. Smooth onboarding flow
5. Trust-building (review section, clear communication)

**Ready to Build**: Yes! This is a solid, feasible MVP that can be enhanced later with live preview if needed.
