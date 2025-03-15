from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Product, Category, Tag


#admin.site.register(Product)
#admin.site.register(Category)
#admin.site.register(Tag)

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class TagResource(resources.ModelResource):
    class Meta:
        model = Tag

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ('id', 'name')

@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ('id', 'name', 'category', 'price')
    list_filter = ('category', 'tags')
    search_fields = ('name', 'description')

