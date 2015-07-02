# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150501_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(db_index=True, verbose_name='Published', default=False),
        ),
    ]
