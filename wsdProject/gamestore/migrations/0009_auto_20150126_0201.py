# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0008_auto_20150126_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='url',
            field=models.URLField(),
            preserve_default=True,
        ),
    ]
