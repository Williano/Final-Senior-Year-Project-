from django.contrib import admin
from .models import Coupon

from import_export.admin import ImportExportModelAdmin

# Customizes the admin backend for the project.

admin.site.site_title = "E-Shopper"
admin.site.site_header = "E-Shopper Administration"
admin.site.index_title = "E-Shopper"


class CouponAdmin(ImportExportModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']


admin.site.register(Coupon, CouponAdmin)
