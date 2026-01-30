# 📸 SwiftCart Screenshots & Page Guide

## Navigation & Layout

### Header / Navbar
- **SwiftCart Logo** (left) - Lightning bolt icon + gradient text
- **Search Bar** (center) - Full-width on desktop, below on mobile
- **Dark Mode Toggle** - Moon/sun icon
- **Wishlist Icon** - Heart icon (logged in users)
- **Cart Icon** - Shopping cart with badge showing item count
- **User Menu** - Profile dropdown or Login/Sign Up buttons

### Footer
- **Brand Section** - Logo and tagline
- **Shop Links** - All Products, Featured, Flash Sales
- **Account Links** - Profile, Orders, Wishlist
- **Social Media** - Facebook, Twitter, Instagram, LinkedIn icons
- **Copyright** - "Built with ❤️ for Hackathons"

## Page-by-Page Description

### 1. Homepage (`/`)
**Hero Section:**
- Purple gradient background
- Large heading: "Welcome to SwiftCart"
- Subheading: "Discover amazing products at unbeatable prices"
- Two CTAs: "Shop Now" and "Explore"

**Categories Section:**
- 6 category cards in grid
- Icon + name for each category
- Hover effect with scale
- Electronics, Fashion, Home & Living, Books, Beauty, Sports

**Flash Sale Section** (if available):
- Red/pink gradient background
- Animated bolt icons
- 4 products with discount badges
- "Limited time offers" text

**Featured Products Section:**
- 8 products in responsive grid
- Product image, name, price
- Category tag
- Discount badge (if applicable)
- Flash sale badge (if applicable)
- Stock status
- "Add to Cart" button

**Features Section:**
- 4 feature highlights in grid
- Free Shipping, Secure Payment, Easy Returns, 24/7 Support
- Icons in purple circles
- Short descriptions

### 2. Product Listing (`/products/`)
**Left Sidebar:**
- Sticky category menu
- "All Products" option
- Individual category links with icons
- Active category highlighted

**Main Content:**
- Page title and product count
- Sort dropdown (Newest, Price, Name)
- Product grid (3 columns desktop)
- Each product card shows:
  - Image with badges
  - Name and category
  - Price (with strikethrough if discounted)
  - "Add to Cart" button
  - Wishlist heart icon (logged in)

**Pagination:**
- First, Previous, Page X of Y, Next, Last buttons
- Maintains search and sort parameters

### 3. Product Detail (`/product/<slug>/`)
**Breadcrumb:**
- Home → Products → Category → Product name

**Left Side:**
- Large product image
- Discount badge (top right)
- Flash sale badge (top left)

**Right Side:**
- Product name (large)
- Category link with icon
- Price display (original + discounted)
- Stock status badge (green/red)
- Product description
- Quantity selector
- "Add to Cart" button (full width)
- Wishlist button (heart icon)
- Trust badges:
  - Free Delivery
  - Secure Payment
  - Easy Returns
  - Support 24/7

**Related Products:**
- 4 similar products from same category
- Smaller cards
- Quick links to details

### 4. Shopping Cart (`/cart/`)
**If Empty:**
- Large cart icon
- "Your cart is empty" message
- "Start Shopping" button

**If Has Items:**
- Left side (2/3 width):
  - List of cart items
  - Each item shows:
    - Product image
    - Name and category
    - Price per unit
    - Quantity input + Update button
    - Remove icon (trash)
    - Line total
  - "Clear Cart" link at bottom

- Right side (1/3 width, sticky):
  - Order summary card
  - Subtotal
  - Shipping (FREE)
  - Total (large, purple)
  - "Proceed to Checkout" button
  - "Continue Shopping" link

### 5. Checkout (`/orders/checkout/`)
**Left Side (2/3):**
- **Shipping Information Form:**
  - Full Name
  - Email
  - Phone
  - Address
  - City, State, Zip
  - Country

- **Payment Method:**
  - Credit Card option (checked)
  - PayPal option
  - Demo notice

**Right Side (1/3, sticky):**
- Order summary
- List of items with quantities
- Subtotal, Shipping, Total
- "Place Order" button with lock icon

### 6. Order Success (`/orders/success/<id>/`)
- Large green checkmark icon
- "Order Placed Successfully!" heading
- "Thank you for your purchase!"
- Order number in highlighted box
- 3 info boxes:
  - Total Amount
  - Status
  - Payment Method
- Two buttons:
  - "View Order Details"
  - "Continue Shopping"

### 7. Order History (`/orders/history/`)
**If Empty:**
- Box icon
- "No orders yet"
- "Start shopping" message and button

**If Has Orders:**
- List of order cards
- Each card shows:
  - Order number and date (left)
  - Total and status badge (right)
  - Item count
  - "View Details" link

### 8. Order Detail (`/orders/detail/<id>/`)
**Left Side:**
- **Order Items:**
  - List of products ordered
  - Name, quantity, price
  - Line totals

- **Shipping Information:**
  - Full address details
  - Contact information

**Right Side (sticky):**
- Order summary card
- Order number
- Date
- Status badge
- Subtotal, shipping, total

### 9. Login (`/accounts/login/`)
- Centered card
- Large user icon (purple)
- "Welcome Back" heading
- Username input
- Password input
- "Login" button with icon
- Link to "Sign Up"

### 10. Register (`/accounts/register/`)
- Centered card
- User plus icon (purple)
- "Create Account" heading
- Username input
- Password input
- Confirm password input
- "Create Account" button with icon
- Link to "Login"

### 11. Profile (`/accounts/profile/`)
**Left Side (1/3):**
- Large user circle icon
- Username and email
- Total orders count (large)
- "View Orders" button
- "Wishlist" button

**Right Side (2/3):**
- "Recent Orders" section
- If no orders: "No orders yet" with shop button
- If has orders: List of order cards
  - Order number, date, total, status
  - Item count
  - "View Details" link
- "View All Orders" link

### 12. Wishlist (`/shop/wishlist/`)
**If Empty:**
- Large heart icon
- "Your wishlist is empty"
- "Add products you love"
- "Browse Products" button

**If Has Items:**
- Product grid (4 columns)
- Each card shows:
  - Product image with badges
  - Remove button (trash icon, top right)
  - Name, category
  - Price (with discount)
  - "Add to Cart" button

### 13. Search Results (`/products/?q=query`)
- Same layout as product listing
- Shows "Found X results for 'query'"
- If no results:
  - Box icon
  - "No products found"
  - "Try adjusting your search"
  - "View All Products" button

## Visual Design Elements

### Color Palette
```
Primary:    #7c3aed (Purple)
Secondary:  #6d28d9 (Dark Purple)
Success:    #10b981 (Green)
Warning:    #f59e0b (Yellow)
Error:      #ef4444 (Red)
Info:       #3b82f6 (Blue)
Gray:       #6b7280 (Text)
Light:      #f9fafb (Background)
Dark:       #1f2937 (Dark mode bg)
```

### Typography
```
Headings:   Bold, 2rem-4rem
Body:       Regular, 1rem
Small:      0.875rem
Labels:     Medium weight, 0.875rem
```

### Spacing
```
Cards:      Padding 1.5rem
Sections:   Margin 3rem
Grid gap:   1.5rem
Form gap:   1rem
```

### Effects
```
Shadows:    Medium on cards, large on hover
Borders:    Rounded-lg (0.5rem)
Transitions: 200ms ease
Hovers:     Scale 1.05, brightness increase
```

## Dark Mode Differences

### Light Mode
- White backgrounds (#ffffff)
- Gray text (#1f2937)
- Light borders (#e5e7eb)
- Gray cards (#f9fafb)

### Dark Mode
- Dark backgrounds (#1f2937)
- Light text (#f9fafb)
- Dark borders (#374151)
- Darker cards (#111827)
- Adjusted contrasts for accessibility

## Responsive Breakpoints

### Mobile (< 640px)
- Single column layouts
- Stacked navigation
- Full-width cards
- Mobile-optimized forms
- Smaller fonts

### Tablet (640px - 1024px)
- 2-column product grids
- Adjusted spacing
- Touch-friendly buttons
- Optimized images

### Desktop (> 1024px)
- 3-4 column grids
- Sidebar layouts
- Hover effects
- Full navigation
- Optimal spacing

## Animation & Interactions

### On Page Load
- Fade in animations
- Slide down effects
- Smooth transitions

### On Hover
- Card lift (translateY)
- Shadow increase
- Color transitions
- Icon animations

### On Click
- Button press effect
- Form submission feedback
- Loading states
- Success/error messages

### Scroll Effects
- Sticky navigation
- Smooth scrolling
- Back to top (implicit)

## Accessibility Features

- ✅ Semantic HTML5 tags
- ✅ ARIA labels where needed
- ✅ Keyboard navigation
- ✅ Focus indicators
- ✅ Color contrast compliance
- ✅ Alt text for images
- ✅ Form labels
- ✅ Error messages

## Browser Compatibility

Tested and works on:
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS/Android)

## Performance Notes

- CDN-loaded assets (Tailwind, Font Awesome)
- Optimized images via Unsplash
- Minimal JavaScript
- Fast page loads
- Database query optimization
- Efficient Django templates

---

**Note**: Actual appearance may vary slightly based on browser and screen size. All screenshots described represent the default installation with sample data loaded.
