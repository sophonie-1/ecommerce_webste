# 🚀 SwiftCart - Modern E-Commerce Platform

![SwiftCart Banner](https://images.unsplash.com/photo-1557821552-17105176677c?w=1200&h=300&fit=crop)

**SwiftCart** is a full-featured, production-ready e-commerce platform built with **Django 6** and **Tailwind CSS v3**. Designed for hackathons and rapid development, it combines beautiful UI/UX with powerful e-commerce features.

## ✨ Key Features

### 🎯 Core E-Commerce Features
- ✅ **User Authentication** - Secure registration, login, and profile management
- ✅ **Product Catalog** - Browse products by category with advanced filtering
- ✅ **Shopping Cart** - Session-based cart with persistent storage
- ✅ **Checkout Process** - Multi-step checkout with order management
- ✅ **Order History** - Track all past orders with detailed information
- ✅ **Wishlist** - Save favorite products for later

### 🎨 Modern UI/UX
- 🌓 **Dark Mode** - Toggle between light and dark themes
- 📱 **Responsive Design** - Perfect on mobile, tablet, and desktop
- ⚡ **Smooth Animations** - Tailwind CSS transitions and transforms
- 🎯 **Intuitive Navigation** - Clean, user-friendly interface
- 🔔 **Toast Notifications** - Real-time feedback for user actions
- 🎨 **Beautiful Cards** - Product cards with hover effects

### 🔥 Advanced Features
- 🔍 **Search Functionality** - Search products by name or description
- 🏷️ **Flash Sales** - Special badges for sale items
- 💰 **Discount System** - Support for discounted prices
- ⭐ **Featured Products** - Highlight special products on homepage
- 📊 **Stock Management** - Real-time stock tracking
- 🛒 **Live Cart Counter** - Dynamic cart badge updates
- 📦 **Category Filtering** - Browse by 6 different categories

### 🎭 Demo Features
- 💳 **Fake Payment** - Simulated payment processing (demo only)
- 📧 **Email Display** - Contact information (demo)
- 🎁 **Free Shipping** - Promotional feature

## 🛠️ Tech Stack

### Backend
- **Django 6.0+** - Latest stable Python web framework
- **SQLite** - Default database (perfect for demos)
- **Django Admin** - Powerful admin interface
- **Class-Based Views** - Clean, reusable code

### Frontend
- **Tailwind CSS v3** - Utility-first CSS framework (CDN)
- **Font Awesome 6** - Beautiful icons
- **Vanilla JavaScript** - No framework overhead
- **Dark Mode Support** - localStorage persistence

### Architecture
- **Session-based Cart** - Works for guests and authenticated users
- **Context Processors** - Global cart availability
- **Django Messages** - User feedback system
- **URL Routing** - RESTful URL structure

## 📦 Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Quick Start (5 minutes)

1. **Clone or Download the Project**
```bash
cd /path/to/swiftcart
```

2. **Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Migrations**
```bash
python manage.py migrate
```

5. **Create Sample Data**
```bash
python manage.py populate_products
```

6. **Create Admin Account**
```bash
python manage.py createsuperuser
# Or use the default admin account:
# Username: admin
# Password: admin123
```

7. **Run Development Server**
```bash
python manage.py runserver
```

8. **Access the Application**
- **Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Default Admin**: `admin` / `admin123`

## 🗂️ Project Structure

```
swiftcart/
├── swiftcart_project/          # Main project configuration
│   ├── settings.py             # Django settings
│   ├── urls.py                 # Main URL routing
│   └── wsgi.py                 # WSGI configuration
│
├── shop/                       # Product catalog app
│   ├── models.py               # Category, Product, Wishlist
│   ├── views.py                # Product views
│   ├── admin.py                # Admin configuration
│   ├── urls.py                 # Shop URLs
│   └── management/
│       └── commands/
│           └── populate_products.py  # Sample data generator
│
├── cart/                       # Shopping cart app
│   ├── models.py               # Cart, CartItem
│   ├── views.py                # Cart operations
│   ├── context_processors.py  # Global cart context
│   └── urls.py                 # Cart URLs
│
├── orders/                     # Order management app
│   ├── models.py               # Order, OrderItem
│   ├── views.py                # Checkout & orders
│   ├── admin.py                # Order admin
│   └── urls.py                 # Order URLs
│
├── accounts/                   # User authentication app
│   ├── views.py                # Auth views
│   └── urls.py                 # Auth URLs
│
├── templates/                  # HTML templates
│   ├── base.html               # Base template with nav/footer
│   ├── shop/                   # Shop templates
│   │   ├── home.html
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   └── wishlist.html
│   ├── cart/
│   │   └── cart.html
│   ├── orders/
│   │   ├── checkout.html
│   │   ├── order_success.html
│   │   ├── order_history.html
│   │   └── order_detail.html
│   └── accounts/
│       ├── login.html
│       ├── register.html
│       └── profile.html
│
├── static/                     # Static files (if needed)
├── media/                      # User uploads (if needed)
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management script
└── requirements.txt            # Python dependencies
```

## 🎮 Usage Guide

### For Users

1. **Browse Products**
   - Visit homepage to see featured products
   - Click categories to filter
   - Use search bar for specific items

2. **Add to Cart**
   - Click "Add to Cart" on any product
   - Adjust quantities in cart
   - Cart badge shows item count

3. **Checkout**
   - Click cart icon → "Proceed to Checkout"
   - Fill shipping information
   - Select payment method (demo)
   - Place order

4. **Account Features**
   - Register/Login from navbar
   - View profile and order history
   - Add products to wishlist
   - Track order status

### For Admins

1. **Access Admin Panel**
   - Navigate to `/admin/`
   - Login with admin credentials

2. **Manage Products**
   - Add/edit/delete products
   - Set featured/flash sale status
   - Update stock levels
   - Upload product images (URLs)

3. **Manage Orders**
   - View all orders
   - Update order status
   - Track customer information

4. **Manage Categories**
   - Create new categories
   - Assign Font Awesome icons
   - Edit descriptions

## 🎨 Customization

### Change Color Scheme

Edit `templates/base.html` (line 26-36):
```javascript
tailwind.config = {
    theme: {
        extend: {
            colors: {
                primary: {
                    600: '#7c3aed',  // Change this to your color
                }
            }
        }
    }
}
```

### Add New Categories

```bash
python manage.py shell
```
```python
from shop.models import Category
Category.objects.create(
    name='Your Category',
    icon='fa-icon-name',  # Font Awesome icon
    description='Category description'
)
```

### Modify Product Data

Run the management command again (safe to run multiple times):
```bash
python manage.py populate_products
```

Or add manually via admin panel.

## 📊 Sample Data

The project includes **18 pre-loaded products** across **6 categories**:
- 📱 **Electronics** (5 products) - Gadgets, TVs, cameras
- 👕 **Fashion** (4 products) - Clothing, accessories
- 🏠 **Home & Living** (3 products) - Furniture, decor
- 📚 **Books** (2 products) - Educational, self-help
- 💄 **Beauty** (2 products) - Cosmetics, perfumes
- ⚽ **Sports** (2 products) - Fitness equipment

All products feature:
- High-quality Unsplash images
- Realistic prices
- Detailed descriptions
- Stock levels
- Some with discounts/flash sales

## 🎯 Hackathon Tips

### Demo Presentation (5 minutes)

1. **Homepage** (30 sec)
   - Show hero banner, categories, featured products
   - Toggle dark mode

2. **Product Browsing** (1 min)
   - Search for products
   - Filter by category
   - Show product details

3. **Shopping Flow** (2 min)
   - Add items to cart
   - Update quantities
   - Complete checkout process
   - Show order confirmation

4. **User Features** (1 min)
   - Register/login
   - View profile
   - Check order history
   - Add to wishlist

5. **Admin Panel** (30 sec)
   - Show product management
   - Order tracking

### Impressive Features to Highlight

✅ Full dark mode support  
✅ Real-time cart updates  
✅ Responsive design  
✅ Search functionality  
✅ Flash sales & discounts  
✅ Order history tracking  
✅ Wishlist feature  
✅ Clean admin interface  

## 🐛 Troubleshooting

### Issue: Static files not loading
```bash
python manage.py collectstatic
```

### Issue: Database errors
```bash
rm db.sqlite3
python manage.py migrate
python manage.py populate_products
```

### Issue: Port already in use
```bash
python manage.py runserver 8080  # Use different port
```

### Issue: Admin can't login
```bash
python manage.py createsuperuser
```

## 🚀 Deployment

### For Production

1. **Update settings.py**
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'your-secret-key'  # Generate new secret key
```

2. **Use PostgreSQL** (recommended)
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'swiftcart',
        # ... other settings
    }
}
```

3. **Collect Static Files**
```bash
python manage.py collectstatic
```

4. **Use Real Payment Gateway**
   - Integrate Stripe/PayPal API
   - Update checkout views

## 📝 License

This project is open-source and free to use for hackathons, learning, and personal projects.

## 🙏 Credits

- **Django Framework** - Web framework
- **Tailwind CSS** - Styling
- **Font Awesome** - Icons
- **Unsplash** - Product images

## 🎓 Learning Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [Django E-Commerce Tutorial](https://www.youtube.com/results?search_query=django+ecommerce)

## 📧 Support

For questions or issues:
- Check Django documentation
- Review code comments
- Debug with `python manage.py runserver --verbosity 3`

---

**Built with ❤️ for Hackathons | SwiftCart © 2024**

*Ready to win your next hackathon? Fork this project and customize it to your needs!* 🏆
