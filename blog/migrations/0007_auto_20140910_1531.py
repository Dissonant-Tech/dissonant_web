# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20140809_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_publish',
            field=models.DateField(verbose_name='Publish Date'),
        ),
    ]
