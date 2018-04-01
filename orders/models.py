from django.db import models
from onlineshop.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator
from django.utils.translation import gettext_lazy as _
from coupons.models import Coupon


class Order(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone Number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    email_regex = RegexValidator(regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

    first_name = models.CharField(_('first name'), max_length=50, blank=False)
    last_name = models.CharField(_('last name'), max_length=50, blank=False)
    email = models.EmailField(_('e-mail'), validators=[email_regex], blank=False)
    phone_number = models.CharField(_('phone number'), validators=[phone_regex], max_length=17, blank=False)
    address = models.CharField(_('address'), max_length=250, blank=False)
    city = models.CharField(_('city'), max_length=100, blank=False)
    state_or_region = models.CharField(_('state or region'), max_length=100, blank=False)
    postal_code = models.CharField(_('postal code'), max_length=5, blank=False)
    country = models.CharField(_('country'), max_length=100, blank=False)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)
    paid = models.BooleanField(_('paid'), default=False)
    coupon = models.ForeignKey(Coupon, related_name='orders', null=True, blank=True)
    discount = models.IntegerField(_('discount'), default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
