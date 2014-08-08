# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary_markdown',
            field=models.TextField(verbose_name='Summary (Markdown)', max_length=765, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='summary_markup',
            field=models.TextField(verbose_name='Summary (Markup)', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='article',
            name='summary',
        ),
    ]
