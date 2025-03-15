from django.db import models

# Category and Tag models are pretty simple, we are just saving their names.
# Product will be related to category as a one to one relationship, one product just have one
# category in this assumption. However one product can be related to multiple tags, that's
# why I'm using ManyToManyField. It's important to say that a product can also have none tags
# hence the blank=True. auto_now_add will save the time and date of the creation of the product.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    tags = models.ManyToManyField(Tag, related_name="products",blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
