# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0001_initial'),
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(verbose_name='first name', max_length=50)),
                ('last_name', models.CharField(verbose_name='last name', max_length=50)),
                ('email', models.EmailField(verbose_name='e-mail', max_length=254, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')])),
                ('phone_number', models.CharField(verbose_name='phone number', max_length=17, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone Number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('address', models.CharField(verbose_name='address', max_length=250)),
                ('city', models.CharField(verbose_name='city', max_length=100)),
                ('state_or_region', models.CharField(verbose_name='state or region', max_length=100)),
                ('postal_code', models.CharField(verbose_name='postal code', max_length=5)),
                ('country', models.CharField(verbose_name='country', max_length=100)),
                ('created', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('updated', models.DateTimeField(verbose_name='updated', auto_now=True)),
                ('paid', models.BooleanField(verbose_name='paid', default=False)),
                ('discount', models.IntegerField(verbose_name='discount', default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('coupon', models.ForeignKey(blank=True, null=True, related_name='orders', to='coupons.Coupon')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('price', models.DecimalField(max_digits=10, decimal_places=2)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(related_name='order_items', to='onlineshop.Product')),
            ],
        ),
    ]
