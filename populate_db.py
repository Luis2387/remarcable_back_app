import os
import django
import random

# Since this is being triggered on deployment, this is necesary for django to know which
# Settings needs to be used

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remarcable_back_app.settings')
django.setup()

from products.models import Category, Tag, Product


# IA generated list of categories, tags and products

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

# Create or retreive if already exists a list of categories based on the list provided

for cat in CATEGORIES:
    category, created = Category.objects.get_or_create(name=cat)

# Create or retreive if already exists a list of tags based on the list provided

for tag in TAGS:
    tag_obj, created = Tag.objects.get_or_create(name=tag)

# Choose ramdonly a category for each product based on the newly created or retreived categories.
# Once that's donde, it creates products based on the randomly choose category and the price and name
# of the list. Finally, if the product is created, it assigns randomly tags between 0 and 3, using
# the newly created or retreived tags.

for name, price in PRODUCTS:
    category = random.choice(Category.objects.all())
    product, created = Product.objects.get_or_create(name=name, defaults={"price": price, "category": category})
    
    if created:
        tags_sample = random.sample(list(Tag.objects.all()), k=random.randint(0, 3))
        product.tags.set(tags_sample)        

