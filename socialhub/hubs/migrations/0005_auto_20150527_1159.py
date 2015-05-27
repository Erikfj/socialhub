# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0004_auto_20150527_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hub',
            name='email',
        ),
        migrations.AddField(
            model_name='hub',
            name='hubpoints',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
