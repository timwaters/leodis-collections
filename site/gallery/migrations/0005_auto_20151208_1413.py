# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20151207_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=djgeojson.fields.PointField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='subject_id',
            field=models.CharField(max_length=128, null=True, blank=True),
        ),
    ]
