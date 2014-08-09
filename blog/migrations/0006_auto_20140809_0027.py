# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(verbose_name='Published', default=False),
        ),
    ]
