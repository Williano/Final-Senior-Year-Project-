# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20180128_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=200, default='Kumasi'),
        ),
        migrations.AddField(
            model_name='order',
            name='zip_code',
            field=models.IntegerField(default=0),
        ),
    ]
