# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_auto_20151219_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='creator',
            field=models.CharField(help_text=b'Keep blank when adding to autofill from Leodis.net', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='centre',
            field=djgeojson.fields.PointField(help_text=b'move map to set default view', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='lat',
            field=models.FloatField(help_text=b'Gets updated when the map is moved', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='lon',
            field=models.FloatField(help_text=b'Gets updated when the map is moved', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='zoom',
            field=models.IntegerField(help_text=b'Gets updated when the map is moved', null=True, blank=True),
        ),
    ]
