# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug', unique=True, help_text='Uri Identifier')),
                ('content_markup', models.TextField(verbose_name='Content (Markup)')),
                ('content_markdown', models.TextField(verbose_name='Content (Markdown)')),
                ('date_publish', models.DateField(verbose_name='Publish Date', auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_publish'],
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=100, unique=True, db_index=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category', verbose_name='Categories', null=True),
            preserve_default=True,
        ),
    ]
