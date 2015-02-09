# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150209_2122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content_markdown',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='summary_markdown',
            new_name='summary',
        ),
    ]
