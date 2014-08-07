# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(help_text='Uri Identifier', unique=True, max_length=255, verbose_name='Slug')),
                ('content_markup', models.TextField(verbose_name='Content (Markup)')),
                ('content_markdown', models.TextField(verbose_name='Content (Markdown)')),
                ('date_publish', models.DateField(auto_now_add=True, verbose_name='Publish Date')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['-date_publish'],
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(unique=True, max_length=100, verbose_name='Title', db_index=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='blog.Category', blank=True, null=True, verbose_name='Categories'),
            preserve_default=True,
        ),
    ]
