# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20150702_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_publish',
            field=models.DateField(db_index=True, verbose_name='Publish Date'),
        ),
    ]
