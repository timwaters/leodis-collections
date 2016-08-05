# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0012_auto_20151230_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(blank=True)),
                ('html', models.CharField(default=b'about', unique=True, max_length=2, choices=[(b'about', b'About Page'), (b'front', b'Front Page About Text')])),
            ],
        ),
    ]
