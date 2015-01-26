# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0009_auto_20150126_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='developer',
            field=models.ForeignKey(to='gamestore.Usertypes'),
            preserve_default=True,
        ),
    ]
