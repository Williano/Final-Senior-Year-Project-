# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_remove_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(max_length=17, default=0, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone Number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
            preserve_default=False,
        ),
    ]
