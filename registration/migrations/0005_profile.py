# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('registration', '0004_supervisedregistrationprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(verbose_name='first name', max_length=50)),
                ('last_name', models.CharField(verbose_name='last name', max_length=50)),
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(blank=True, null=True, default='media/avatar.jpg', help_text='Your photo (not an illustration nor avatar), It will be published on the website. Ideal photo is: a head shot, shows only you, has no “filters” applied and is as large and uncompressed as possible. We might crop it and change contrast, brightness etc. to fit our visual style.', upload_to='user_accounts')),
                ('bio', models.TextField(max_length=500, help_text='Tell us a bit about yourself')),
                ('email', models.EmailField(verbose_name='e-mail', max_length=254)),
                ('phone_number', models.CharField(verbose_name='phone number', max_length=17, help_text='Please include your country code.', validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{9,15}$', message="Phone Number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('address', models.CharField(verbose_name='address', max_length=250)),
                ('city', models.CharField(verbose_name='city', max_length=100)),
                ('state_or_region', models.CharField(verbose_name='state or region', max_length=100)),
                ('postal_code', models.CharField(verbose_name='postal code', max_length=5)),
                ('country', models.CharField(verbose_name='country', max_length=100)),
            ],
        ),
    ]
