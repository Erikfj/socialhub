# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hubs', '0002_hub'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hub',
            old_name='name',
            new_name='topic',
        ),
        migrations.RemoveField(
            model_name='hub',
            name='hobby',
        ),
        migrations.RemoveField(
            model_name='hub',
            name='owned_points',
        ),
        migrations.AlterField(
            model_name='hub',
            name='email',
            field=models.TextField(),
        ),
    ]
