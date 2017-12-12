from django.contrib import admin
from .models import Category, Product


# Customizes the admin backend for the project.

admin.site.site_title = "E-Shopper"
admin.site.site_header = "E-Shopper Administration"
admin.site.index_title = "E-Shopper"

# Registers the Category model in the admin site.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


# Registers the Product model in the admin site.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category','price',
                    'stock', 'available', 'created',
                    'updated',
                    ]
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


