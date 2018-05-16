import csv
import datetime
from django.contrib import admin
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Order, OrderItem
from import_export.admin import ImportExportModelAdmin

# Customizes the admin backend for the project.

admin.site.site_title = "E-Shopper"
admin.site.site_header = "E-Shopper Administration"
admin.site.index_title = "E-Shopper"


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    # write the header row
    writer.writerow([field.verbose_name for field in fields])
    # write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response


export_to_csv.short_description = 'Export to CSV'


def order_detail(obj):
    return '<a href="{}">View</a>'.format(reverse('orders:admin_order_detail',
                                                  args=[obj.id]))


order_detail.allow_tags = True


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(ImportExportModelAdmin):
    list_display = ['id',
                    'first_name',
                    'last_name',
                    'email',
                    'phone_number',
                    'address',
                    'city',
                    'country',
                    'paid',
                    'created',
                    'updated',
                    order_detail,]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = [export_to_csv]

admin.site.register(Order, OrderAdmin)
