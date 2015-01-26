# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0007_auto_20150126_0158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='name',
            field=models.CharField(unique=True, max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='games',
            name='url',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
