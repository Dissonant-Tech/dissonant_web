# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20140808_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary_markdown',
            field=models.TextField(verbose_name='Summary (Markdown)', max_length=765),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary_markup',
            field=models.TextField(verbose_name='Summary (Markup)'),
        ),
    ]
