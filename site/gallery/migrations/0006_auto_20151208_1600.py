# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20151208_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='photo',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
