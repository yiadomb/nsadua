# PRD Analysis: nsadua.com Sash Customization Platform

## My Understanding of the System

### Core Concept
A WordPress-based e-commerce platform where students can customize graduation sashes (stoles) with their school information, logos, and personal details. The key differentiator is a **live, interactive preview editor** built with React and Fabric.js that shows real-time customization as students fill out their information.

### Architecture Overview

#### 1. **Platform Stack**
- **CMS/Pages**: WordPress.com Business + Elementor Pro
- **Editor**: React SPA with Fabric.js canvas
- **Assets**: AWS S3 + CloudFront CDN
- **E-commerce**: WooCommerce
- **Integration**: React embedded via shortcode/HTML widget

#### 2. **Two Entry Paths**

**Path A: Gallery/Homepage → Direct Template Selection**
- User clicks any sash image (homepage hero, gallery, blog)
- Each image has a database pointer to its template ID
- Modal/page appears with "I Want This Sash" button
- Opens Fabric.js editor with that specific template pre-loaded and locked
- Bottom drawer appears (non-dismissible) requiring:
  - School/Institution
  - Programme
  - Department/College
  - Name
- As fields are filled, editor auto-populates logos and text in real-time

**Path B: Direct Customization**
- User clicks "Customise" link/menu
- Short onboarding form (Occasion, School, Programme, Department, Name)
- Data stored in session
- Editor opens with default Ghana-Flag sash template
- Details auto-populated
- Option to "Browse Other Templates" → opens Template Chooser

#### 3. **Auto-Population Logic**

**Logo Auto-Insertion:**
- When School + Department provided → automatically inserts 2-logo combo
  - School crest (left)
  - Department crest (right)
- Tooltip: "Default logos added, tap to change"
- If multiple department logos exist → mini-carousel/dropdown for swapping
- Students can tap any logo to replace/edit

**Programme Text:**
- Auto-complete dropdown as user types
- Suggests formats like "BSc Electrical Engineering 2025"
- Falls back to exact user input if no match
- Real-time preview updates

**Name Field:**
- Placeholder: "Miss. Rosemond K. Dei"
- Helper text: "Titles (Mr., Miss, Dr.) are optional"
- Real-time preview

#### 4. **Template Chooser**
- Grid layout of sash templates
- Filtered by student's school context (from onboarding)
- Each card shows:
  - Thumbnail (200x250px)
  - Semi-transparent badges: Name, Category, Price
- Responsive: 2 cards (mobile), 4 (tablet), multiple (desktop)
- Clicking thumbnail → "I Want This Sash" → loads template into editor
- Search/Show All fallback

#### 5. **Photo-Based Backgrounds**

**Asset Specifications:**
- Canvas: 1300x250 pixels
- Thumbnails: 200x250 pixels
- Format: PNG
- File size: 50-100KB (optimized)
- Source: High-res photos of blank sashes (cropped/straightened)

**Editor Behavior:**
- Fetches template record (background URL)
- Creates Fabric.js image object
- Scales to canvas width
- Sets as unselectable/locked
- Students add logos/text on top

**Safe Areas:**
- Template metadata defines normalized rectangles (relative to canvas)
- Admin UI to draw/adjust safe area overlays
- Editor enforces constraints (objects can't move/resize outside zones)
- Two logo zones: Zone A and Zone B
- Drag-and-drop swapping: dropping logo in opposite zone swaps positions
- Visual feedback on hover

#### 6. **Template Library Management**

**Admin Workflow:**
- Drag-and-drop photo uploads
- Tag with: Name, Category, Price
- Add metadata (safe areas, logo zones)
- Auto-generate thumbnails
- Live preview of how thumbnails appear
- Explicit publish step

**Student Workflow:**
- Browse filtered list (by school/department)
- View thumbnails with price/category overlays
- Select sash → populates in editor

#### 7. **Pricing Engine**

**Structure:**
- Template-driven, flat-rate pricing
- Each template has fixed price field (e.g., 150 GHS)
- Delivery fee: Standard (20 GHS) or Express (35 GHS)
- Pricing API: POST request (template ID + delivery option) → returns total breakdown
- Price badge updates instantly in editor
- Admin panel: edit price input + delivery fee table

#### 8. **Asset Hosting**

**Infrastructure:**
- S3 bucket: sash photos, templates, logos, adinkra symbols
- WP Offload Media plugin: syncs Media Library → S3 + CloudFront
- React frontend: fetches via CloudFront signed URLs
- React bundle: versioned in theme assets OR served via S3/CloudFront

#### 9. **Page Structure (Mobile-First)**

1. **Home**: Marketing hero, mission blurb, CTA to customise, 3-4 sash images (linked to Template IDs)
2. **Gallery**: Elementor Pro gallery widget, clicking image opens modal
3. **Customise Landing**: Onboarding form, auto-redirect logic, React block embedded
4. **Editor**: React SPA, mobile canvas fixed at top 40% of screen
5. **Template Chooser**: React sub-view, lazy-loaded thumbnails
6. **Checkout**: WooCommerce + Elementor, pricing API injection, hide unrelated fields
7. **Success/Thank You**: Custom WooCommerce template, order number + delivery ETA
8. **Blog Posts**: Single post templates
9. **About Us**: Footer link
10. **Contact**: Form → support inbox
11. **FAQ**: Mobile collapsible sections
12. **Terms/Privacy**: Static template pages
13. **404**: Friendly page suggesting Home/Gallery

**Build Order**: Home → Customise → Editor → Checkout → Gallery → Static pages

---

## Feasibility Assessment

### ✅ **Highly Feasible Components**

1. **Fabric.js Canvas Editor**: Well-established library, perfect for this use case
2. **React SPA**: Standard approach, can be embedded in WordPress
3. **AWS S3/CloudFront**: Industry standard, WP Offload Media handles integration
4. **Template System**: Straightforward database structure
5. **WooCommerce Integration**: Mature platform, highly customizable
6. **Mobile-First Design**: Essential and achievable
7. **Safe Area Constraints**: Fabric.js supports object constraints

### ⚠️ **Challenges & Considerations**

#### 1. **WordPress.com Business Limitations**
**Issue**: WordPress.com Business has restrictions on:
- Custom plugins (may need approval)
- File system access
- Custom PHP code execution
- Database direct access

**Recommendation**: 
- **Option A**: Use self-hosted WordPress (more flexibility)
- **Option B**: If must use WordPress.com, consider:
  - Host React app externally (separate domain/subdomain)
  - Use WordPress REST API for data
  - Use iframe embedding (less ideal UX)

#### 2. **React Embedding in WordPress**
**Challenge**: Embedding React SPA in WordPress while maintaining:
- State management across page loads
- Session persistence
- Asset loading performance

**Solution**:
- Build React app as standalone bundle
- Use WordPress shortcode that injects `<div id="sash-editor"></div>`
- React mounts to that div
- Use WordPress REST API or custom endpoints for data
- Consider React Router for SPA navigation within editor

#### 3. **Session Management**
**Challenge**: Storing onboarding data across page transitions

**Solutions**:
- **Option A**: localStorage/sessionStorage (client-side, simple)
- **Option B**: WordPress session/cookies (server-side, more secure)
- **Option C**: URL parameters (shareable, but can get messy)
- **Recommendation**: Hybrid - localStorage for UX, WordPress session for checkout

#### 4. **Logo Auto-Matching Logic**
**Challenge**: Automatically matching School + Department to correct logos

**Requirements**:
- Logo library database (School logos, Department logos)
- Matching algorithm (exact match, fuzzy match, fallback)
- Handling missing logos gracefully
- Admin interface for logo management

**Recommendation**:
- Database structure:
  ```
  schools: id, name, logo_url
  departments: id, name, school_id, logo_url
  logo_assignments: template_id, zone (A/B), logo_type (school/department), entity_id
  ```
- Matching: Exact name match first, then fuzzy matching
- Fallback: Generic placeholder or school logo only

#### 5. **Template Metadata Structure**
**Recommendation**:
```json
{
  "id": 123,
  "name": "Ghana Flag Sash",
  "category": "patriotic",
  "price": 150,
  "background_url": "https://cdn.../ghana-flag.png",
  "canvas_dimensions": {"width": 1300, "height": 250},
  "safe_areas": [
    {
      "id": "zone_a",
      "type": "logo",
      "bounds": {"x": 0.1, "y": 0.2, "width": 0.3, "height": 0.6},
      "default_logo_type": "school"
    },
    {
      "id": "zone_b",
      "type": "logo",
      "bounds": {"x": 0.6, "y": 0.2, "width": 0.3, "height": 0.6},
      "default_logo_type": "department"
    },
    {
      "id": "text_zone",
      "type": "text",
      "bounds": {"x": 0.2, "y": 0.1, "width": 0.6, "height": 0.3}
    }
  ],
  "text_defaults": {
    "programme": {"font": "Arial", "size": 24, "color": "#000000"},
    "name": {"font": "Arial", "size": 20, "color": "#000000"}
  }
}
```

#### 6. **Real-Time Preview Performance**
**Challenge**: Updating canvas as user types (could be laggy)

**Optimization Strategies**:
- Debounce text input (update preview after 300ms pause)
- Use React.memo for canvas component
- Virtualize template chooser thumbnails
- Lazy load logos
- Cache template metadata

#### 7. **CloudFront Signed URLs**
**Challenge**: Security + complexity

**Recommendation**:
- Use WP Offload Media for automatic signed URL generation
- Or implement custom endpoint that generates signed URLs server-side
- Cache signed URLs client-side (they expire, but can cache for session)

#### 8. **WooCommerce Customization**
**Challenge**: Injecting custom pricing + hiding standard fields

**Solution**:
- Use WooCommerce hooks/filters:
  - `woocommerce_cart_item_price` - modify displayed price
  - `woocommerce_add_cart_item_data` - store template ID
  - Custom checkout fields
  - Override templates for order confirmation

#### 9. **Database Schema Considerations**

**Recommended Tables**:
```sql
-- Templates
wp_sash_templates (id, name, category, price, background_url, metadata_json, published, created_at)

-- Schools & Departments
wp_schools (id, name, logo_url, created_at)
wp_departments (id, school_id, name, logo_url, created_at)

-- Logo Library
wp_logos (id, type, entity_id, url, created_at)

-- Orders (extends WooCommerce)
wp_sash_orders (order_id, template_id, customization_data_json, delivery_option)

-- Template-School Associations (for filtering)
wp_template_school_associations (template_id, school_id, priority)
```

---

## Suggested Improvements & Alternatives

### 1. **Alternative: Self-Hosted WordPress**
**Why**: More flexibility for custom plugins, better performance, full control
**Trade-off**: Need hosting management, but more cost-effective long-term

### 2. **Logo Matching Enhancement**
**Current**: Auto-match based on School + Department
**Enhancement**: 
- Add "Recent logos" quick-select
- Allow students to search logo library
- Show logo previews in dropdown

### 3. **Template Filtering Enhancement**
**Current**: Filter by school context
**Enhancement**:
- Filter by category (patriotic, academic, custom)
- Filter by price range
- Sort by popularity/recent
- "Recommended for you" based on school

### 4. **Editor UX Improvements**
- Undo/Redo functionality
- Zoom controls (especially for mobile)
- Text formatting toolbar (bold, italic, colors)
- Logo library browser within editor
- Save draft functionality (localStorage)

### 5. **Performance Optimizations**
- Preload popular templates
- Image lazy loading in gallery
- Service worker for offline template caching
- CDN for React bundle

### 6. **Admin Panel Enhancements**
- Bulk template upload
- Template preview with sample data
- Analytics: popular templates, conversion rates
- Logo upload with auto-cropping/resizing

### 7. **Checkout Flow Improvement**
- Show preview thumbnail in cart
- Allow editing from cart
- Save customization as "design" (reusable)
- Share design link (social sharing)

### 8. **Mobile-Specific Considerations**
- Touch-optimized drag handles
- Larger tap targets
- Swipe gestures for template carousel
- Bottom sheet for mobile editor controls

### 9. **Error Handling & Edge Cases**
- What if logo not found? (Show placeholder, allow upload)
- What if template fails to load? (Fallback template)
- What if student enters invalid school? (Suggest similar, allow custom)
- Network failure during save? (Local draft, retry mechanism)

### 10. **Accessibility**
- Keyboard navigation in editor
- Screen reader support
- High contrast mode
- Font size controls

---

## Technical Architecture Recommendation

### **Recommended Stack (Revised)**

1. **WordPress**: Self-hosted (not WordPress.com) for flexibility
2. **Theme**: Custom theme or child theme of lightweight base
3. **Page Builder**: Elementor Pro (as specified) OR consider Gutenberg blocks
4. **Editor**: React SPA (separate build, embedded via shortcode)
5. **State Management**: React Context API or Zustand (lightweight)
6. **API**: WordPress REST API + custom endpoints
7. **Assets**: S3 + CloudFront (as specified)
8. **E-commerce**: WooCommerce (as specified)
9. **Database**: MySQL (WordPress default) + custom tables

### **Build Phases**

**Phase 1: Foundation**
- WordPress setup + custom plugin structure
- Database schema
- Basic React editor (Fabric.js integration)
- Template upload/admin interface

**Phase 2: Core Editor**
- Safe area constraints
- Logo placement/swapping
- Text editing
- Auto-population logic

**Phase 3: Template System**
- Template chooser
- Filtering logic
- Thumbnail generation
- Gallery integration

**Phase 4: Integration**
- WooCommerce customization
- Checkout flow
- Order management
- Pricing API

**Phase 5: Polish**
- Mobile optimization
- Performance tuning
- Error handling
- Analytics

---

## Conclusion

**Overall Feasibility**: ✅ **Highly Feasible**

The PRD describes a well-thought-out system that is technically achievable. The main considerations are:

1. **WordPress.com Business limitations** - recommend self-hosted
2. **React integration complexity** - manageable with proper architecture
3. **Logo matching logic** - requires careful database design
4. **Performance optimization** - critical for mobile experience

The concept is solid, and with the suggested improvements, this could be a robust, scalable platform.

**Next Steps**: 
1. Confirm hosting approach (self-hosted vs WordPress.com)
2. Finalize database schema
3. Create detailed technical specification
4. Begin Phase 1 development
