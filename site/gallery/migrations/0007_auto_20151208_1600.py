# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20151208_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='importance',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='importance',
        ),
    ]
