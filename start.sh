#!/bin/bash

# SwiftCart Quick Start Script
# This script sets up and runs the SwiftCart e-commerce platform

echo "🚀 SwiftCart Quick Start"
echo "========================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt --quiet

# Run migrations
echo "🗄️  Setting up database..."
python manage.py migrate --no-input

# Populate sample data if needed
if [ ! -f "db.sqlite3" ] || [ $(python manage.py shell -c "from shop.models import Product; print(Product.objects.count())" 2>/dev/null) -eq 0 ]; then
    echo "🎨 Creating sample data..."
    python manage.py populate_products
fi

# Create superuser if it doesn't exist
echo "👤 Setting up admin account..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@swiftcart.com', 'admin123')
    print('Admin user created: admin/admin123')
else:
    print('Admin user already exists: admin/admin123')
EOF

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Quick Info:"
echo "   - Website: http://127.0.0.1:8000/"
echo "   - Admin: http://127.0.0.1:8000/admin/"
echo "   - Username: admin"
echo "   - Password: admin123"
echo ""
echo "🚀 Starting development server..."
echo ""

# Start the development server
python manage.py runserver
