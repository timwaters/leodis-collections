# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_auto_20151219_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='lat',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='lon',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='zoom',
            field=models.IntegerField(help_text=b'This gets updated when the map is moved', null=True, blank=True),
        ),
    ]
