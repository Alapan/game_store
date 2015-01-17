# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0002_auto_20150115_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertypes',
            name='usertype',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
