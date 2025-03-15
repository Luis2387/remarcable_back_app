import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remarcable_back_app.settings')
django.setup()

from products.models import Category, Tag, Product


CATEGORIES = ["Electronics", "Books", "Clothing", "Home Appliances", "Toys"]
TAGS = ["New", "Sale", "Limited Edition", "Popular", "Featured", "Best Seller", "Eco-Friendly", "Discount", "Exclusive", "Handmade"]
PRODUCTS = [
    ("Laptop", 999.99),
    ("Smartphone", 699.99),
    ("Bluetooth Speaker", 129.99),
    ("Washing Machine", 399.99),
    ("Microwave Oven", 149.99),
    ("Coffee Maker", 89.99),
    ("Electric Scooter", 499.99),
    ("Wireless Headphones", 199.99),
    ("Smart Watch", 249.99),
    ("Digital Camera", 549.99),
    ("Gaming Console", 599.99),
    ("Board Game", 39.99),
    ("E-Book Reader", 129.99),
    ("Kitchen Blender", 79.99),
    ("Vacuum Cleaner", 179.99),
    ("LED TV", 899.99),
    ("Air Conditioner", 699.99),
    ("Hair Dryer", 39.99),
    ("Desk Lamp", 24.99),
    ("Portable Charger", 49.99),
]

for cat in CATEGORIES:
    category, created = Category.objects.get_or_create(name=cat)

for tag in TAGS:
    tag_obj, created = Tag.objects.get_or_create(name=tag)

for name, price in PRODUCTS:
    category = random.choice(Category.objects.all())
    product, created = Product.objects.get_or_create(name=name, defaults={"price": price, "category": category})
    
    if created:
        tags_sample = random.sample(list(Tag.objects.all()), k=random.randint(0, 3))
        product.tags.set(tags_sample)        

