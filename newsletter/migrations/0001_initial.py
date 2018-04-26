# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import django.contrib.sites.managers
import sorl.thumbnail.fields
from django.conf import settings
import newsletter.utils
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('sortorder', models.PositiveIntegerField(verbose_name='sort order', db_index=True, help_text='Sort order determines the order in which articles are concatenated in a post.')),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('text', models.TextField(verbose_name='text')),
                ('url', models.URLField(verbose_name='link', blank=True, null=True)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='image', blank=True, null=True, upload_to='newsletter/images/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
                'ordering': ('sortorder',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title', max_length=200)),
                ('slug', models.SlugField(verbose_name='slug')),
                ('date_create', models.DateTimeField(verbose_name='created', auto_now_add=True)),
                ('date_modify', models.DateTimeField(verbose_name='modified', auto_now=True)),
            ],
            options={
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='newsletter title', max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('email', models.EmailField(verbose_name='e-mail', max_length=254, help_text='Sender e-mail')),
                ('sender', models.CharField(verbose_name='sender', max_length=200, help_text='Sender name')),
                ('visible', models.BooleanField(verbose_name='visible', db_index=True, default=True)),
                ('send_html', models.BooleanField(verbose_name='send html', default=True, help_text='Whether or not to send HTML versions of e-mails.')),
                ('site', models.ManyToManyField(default=newsletter.utils.get_default_sites, to='sites.Site')),
            ],
            options={
                'verbose_name': 'newsletter',
                'verbose_name_plural': 'newsletters',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('publish_date', models.DateTimeField(verbose_name='publication date', blank=True, null=True, db_index=True, default=django.utils.timezone.now)),
                ('publish', models.BooleanField(verbose_name='publish', db_index=True, default=True, help_text='Publish in archive.')),
                ('prepared', models.BooleanField(verbose_name='prepared', db_index=True, default=False, editable=False)),
                ('sent', models.BooleanField(verbose_name='sent', db_index=True, default=False, editable=False)),
                ('sending', models.BooleanField(verbose_name='sending', db_index=True, default=False, editable=False)),
                ('message', models.ForeignKey(verbose_name='message', to='newsletter.Message')),
                ('newsletter', models.ForeignKey(verbose_name='newsletter', editable=False, to='newsletter.Newsletter')),
            ],
            options={
                'verbose_name': 'submission',
                'verbose_name_plural': 'submissions',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name_field', models.CharField(verbose_name='name', max_length=30, blank=True, null=True, help_text='optional', db_column='name')),
                ('email_field', models.EmailField(verbose_name='e-mail', max_length=254, blank=True, null=True, db_index=True, db_column='email')),
                ('ip', models.GenericIPAddressField(verbose_name='IP address', blank=True, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('activation_code', models.CharField(verbose_name='activation code', max_length=40, default=newsletter.utils.make_activation_code)),
                ('subscribed', models.BooleanField(verbose_name='subscribed', db_index=True, default=False)),
                ('subscribe_date', models.DateTimeField(verbose_name='subscribe date', blank=True, null=True)),
                ('unsubscribed', models.BooleanField(verbose_name='unsubscribed', db_index=True, default=False)),
                ('unsubscribe_date', models.DateTimeField(verbose_name='unsubscribe date', blank=True, null=True)),
                ('newsletter', models.ForeignKey(verbose_name='newsletter', to='newsletter.Newsletter')),
                ('user', models.ForeignKey(verbose_name='user', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'subscription',
                'verbose_name_plural': 'subscriptions',
            },
        ),
        migrations.AddField(
            model_name='submission',
            name='subscriptions',
            field=models.ManyToManyField(verbose_name='recipients', blank=True, db_index=True, help_text='If you select none, the system will automatically find the subscribers for you.', to='newsletter.Subscription'),
        ),
        migrations.AddField(
            model_name='message',
            name='newsletter',
            field=models.ForeignKey(verbose_name='newsletter', to='newsletter.Newsletter'),
        ),
        migrations.AddField(
            model_name='article',
            name='post',
            field=models.ForeignKey(verbose_name='message', related_name='articles', to='newsletter.Message'),
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together=set([('user', 'email_field', 'newsletter')]),
        ),
        migrations.AlterUniqueTogether(
            name='message',
            unique_together=set([('slug', 'newsletter')]),
        ),
    ]
