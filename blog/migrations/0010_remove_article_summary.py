# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150209_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='summary',
        ),
    ]
