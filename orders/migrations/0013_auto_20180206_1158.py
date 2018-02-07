# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_order_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state_or_region',
            field=models.CharField(max_length=100, default='Ashanti'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.RegexValidator(regex='^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$')]),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=5, default=0),
        ),
    ]
