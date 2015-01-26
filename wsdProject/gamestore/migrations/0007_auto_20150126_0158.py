# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0006_usertypes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='name',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
