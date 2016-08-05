# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20151208_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(help_text=b'Keep blank when adding to autofill from Leodis.net', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='subject_id',
            field=models.CharField(help_text=b'Keep blank when adding to autofill from Leodis.net', max_length=128, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='title',
            field=models.CharField(help_text=b'Keep blank when adding to autofill from Leodis.net', max_length=255, blank=True),
        ),
    ]
