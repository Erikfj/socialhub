# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('hobby', models.CharField(max_length=255)),
                ('owned_points', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
