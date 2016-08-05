# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20151212_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='center',
            field=djgeojson.fields.PointField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='zoom',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
