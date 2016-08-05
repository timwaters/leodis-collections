# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_auto_20151219_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='center',
            new_name='centre',
        ),
    ]
