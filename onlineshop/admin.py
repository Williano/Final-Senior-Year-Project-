from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Category, Product, Review
from import_export.admin import ImportExportModelAdmin

# Customizes the admin backend for the project.

admin.site.site_title = "Admin"
admin.site.site_header = "E-Shopper Administration"
admin.site.index_title = "E-Shopper"

# Registers the Category model in the admin site.


class CategoryAdmin(TranslatableAdmin, ImportExportModelAdmin):
    list_display = ['name', 'slug']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(TranslatableAdmin, ImportExportModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available']

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'product', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')


admin.site.register(Review, ReviewAdmin)
