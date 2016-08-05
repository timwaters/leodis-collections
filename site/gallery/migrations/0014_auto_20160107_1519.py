# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0013_site'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Site',
            new_name='SiteCopy',
        ),
    ]
