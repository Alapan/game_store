# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0019_auto_20150211_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='description',
            field=models.CharField(default='description goes here', max_length=250),
            preserve_default=True,
        ),
    ]
