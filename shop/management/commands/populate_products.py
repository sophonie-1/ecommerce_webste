from django.core.management.base import BaseCommand
from shop.models import Category, Product
import random


class Command(BaseCommand):
    help = 'Populate database with sample products'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating categories...')
        
        # Categories with icons
        categories_data = [
            {'name': 'Electronics', 'icon': 'fa-laptop', 'description': 'Latest gadgets and electronics'},
            {'name': 'Fashion', 'icon': 'fa-tshirt', 'description': 'Trendy clothing and accessories'},
            {'name': 'Home & Living', 'icon': 'fa-home', 'description': 'Make your home beautiful'},
            {'name': 'Books', 'icon': 'fa-book', 'description': 'Read and explore'},
            {'name': 'Beauty', 'icon': 'fa-heart', 'description': 'Cosmetics and skincare'},
            {'name': 'Sports', 'icon': 'fa-basketball-ball', 'description': 'Stay fit and active'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'icon': cat_data['icon'],
                    'description': cat_data['description']
                }
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {category.name}'))
        
        self.stdout.write('Creating products...')
        
        # Sample products with Unsplash images
        products_data = [
            # Electronics
            {
                'name': 'Wireless Noise-Canceling Headphones',
                'category': 'Electronics',
                'price': 299.99,
                'discount_price': 249.99,
                'description': 'Premium wireless headphones with active noise cancellation, 30-hour battery life, and superior sound quality.',
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500&h=500&fit=crop',
                'stock': 50,
                'featured': True,
                'flash_sale': True,
            },
            {
                'name': 'Smart Watch Series 7',
                'category': 'Electronics',
                'price': 399.99,
                'discount_price': 349.99,
                'description': 'Advanced smartwatch with fitness tracking, heart rate monitor, GPS, and water resistance.',
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&h=500&fit=crop',
                'stock': 75,
                'featured': True,
            },
            {
                'name': '4K Ultra HD Smart TV 55"',
                'category': 'Electronics',
                'price': 799.99,
                'discount_price': 699.99,
                'description': 'Stunning 4K picture quality with HDR, built-in streaming apps, and voice control.',
                'image_url': 'https://images.unsplash.com/photo-1593359677879-a4bb92f829d1?w=500&h=500&fit=crop',
                'stock': 30,
                'flash_sale': True,
            },
            {
                'name': 'Professional DSLR Camera',
                'category': 'Electronics',
                'price': 1299.99,
                'discount_price': None,
                'description': '24MP full-frame sensor, 4K video recording, dual card slots, weather-sealed body.',
                'image_url': 'https://images.unsplash.com/photo-1516035069371-29a1b244cc32?w=500&h=500&fit=crop',
                'stock': 20,
                'featured': True,
            },
            {
                'name': 'Bluetooth Speaker Premium',
                'category': 'Electronics',
                'price': 149.99,
                'discount_price': 119.99,
                'description': 'Portable wireless speaker with 360° sound, waterproof design, and 20-hour battery.',
                'image_url': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=500&h=500&fit=crop',
                'stock': 100,
            },
            
            # Fashion
            {
                'name': 'Classic Leather Jacket',
                'category': 'Fashion',
                'price': 249.99,
                'discount_price': 199.99,
                'description': 'Premium genuine leather jacket with classic design, perfect for any occasion.',
                'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500&h=500&fit=crop',
                'stock': 45,
                'featured': True,
            },
            {
                'name': 'Designer Sunglasses',
                'category': 'Fashion',
                'price': 189.99,
                'discount_price': 149.99,
                'description': 'UV protection, polarized lenses, stylish frames for men and women.',
                'image_url': 'https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=500&h=500&fit=crop',
                'stock': 80,
                'flash_sale': True,
            },
            {
                'name': 'Running Sneakers Pro',
                'category': 'Fashion',
                'price': 129.99,
                'discount_price': 99.99,
                'description': 'Lightweight, breathable, perfect cushioning for long-distance running.',
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&h=500&fit=crop',
                'stock': 120,
                'featured': True,
            },
            {
                'name': 'Luxury Handbag',
                'category': 'Fashion',
                'price': 349.99,
                'discount_price': None,
                'description': 'Elegant designer handbag with multiple compartments and premium materials.',
                'image_url': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500&h=500&fit=crop',
                'stock': 35,
            },
            
            # Home & Living
            {
                'name': 'Modern Table Lamp',
                'category': 'Home & Living',
                'price': 79.99,
                'discount_price': 59.99,
                'description': 'Sleek design with adjustable brightness, perfect for bedside or office desk.',
                'image_url': 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=500&h=500&fit=crop',
                'stock': 90,
            },
            {
                'name': 'Ergonomic Office Chair',
                'category': 'Home & Living',
                'price': 299.99,
                'discount_price': 249.99,
                'description': 'Lumbar support, adjustable height and armrests, breathable mesh back.',
                'image_url': 'https://images.unsplash.com/photo-1580480055273-228ff5388ef8?w=500&h=500&fit=crop',
                'stock': 40,
                'featured': True,
            },
            {
                'name': 'Luxury Bedding Set',
                'category': 'Home & Living',
                'price': 149.99,
                'discount_price': 119.99,
                'description': '100% Egyptian cotton, king size, includes duvet cover, sheets, and pillowcases.',
                'image_url': 'https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?w=500&h=500&fit=crop',
                'stock': 60,
            },
            
            # Books
            {
                'name': 'The Art of Programming',
                'category': 'Books',
                'price': 49.99,
                'discount_price': 39.99,
                'description': 'Comprehensive guide to software development and best practices.',
                'image_url': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=500&h=500&fit=crop',
                'stock': 150,
            },
            {
                'name': 'Mindfulness & Meditation',
                'category': 'Books',
                'price': 24.99,
                'discount_price': None,
                'description': 'Learn techniques for stress relief and inner peace.',
                'image_url': 'https://images.unsplash.com/photo-1544947950-fa07a98d237f?w=500&h=500&fit=crop',
                'stock': 200,
                'featured': True,
            },
            
            # Beauty
            {
                'name': 'Luxury Perfume Set',
                'category': 'Beauty',
                'price': 129.99,
                'discount_price': 99.99,
                'description': 'Collection of three signature fragrances in elegant bottles.',
                'image_url': 'https://images.unsplash.com/photo-1541643600914-78b084683601?w=500&h=500&fit=crop',
                'stock': 85,
                'flash_sale': True,
            },
            {
                'name': 'Professional Makeup Kit',
                'category': 'Beauty',
                'price': 89.99,
                'discount_price': 69.99,
                'description': 'Complete makeup set with brushes, palettes, and premium products.',
                'image_url': 'https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=500&h=500&fit=crop',
                'stock': 70,
            },
            
            # Sports
            {
                'name': 'Yoga Mat Premium',
                'category': 'Sports',
                'price': 49.99,
                'discount_price': 39.99,
                'description': 'Extra thick, non-slip, eco-friendly material with carrying strap.',
                'image_url': 'https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=500&h=500&fit=crop',
                'stock': 110,
            },
            {
                'name': 'Dumbbell Set Adjustable',
                'category': 'Sports',
                'price': 199.99,
                'discount_price': 169.99,
                'description': 'Adjustable weight from 5-50 lbs, space-saving design for home gym.',
                'image_url': 'https://images.unsplash.com/photo-1517836357463-d25dfeac3438?w=500&h=500&fit=crop',
                'stock': 55,
                'featured': True,
            },
        ]
        
        created_count = 0
        for product_data in products_data:
            category_name = product_data.pop('category')
            product_data['category'] = categories[category_name]
            
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully created {created_count} products!'))
        self.stdout.write(self.style.SUCCESS(f'Total products in database: {Product.objects.count()}'))
