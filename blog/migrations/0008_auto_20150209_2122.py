# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20140910_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content_markup',
        ),
        migrations.RemoveField(
            model_name='article',
            name='summary_markup',
        ),
    ]
