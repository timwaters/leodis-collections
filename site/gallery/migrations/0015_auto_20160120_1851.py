# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0014_auto_20160107_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitecopy',
            name='html',
            field=models.CharField(default=b'about', unique=True, max_length=2, choices=[(b'ab', b'About Page'), (b'fr', b'Front Page About Text')]),
        ),
    ]
