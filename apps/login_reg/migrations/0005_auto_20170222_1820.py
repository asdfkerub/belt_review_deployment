# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 02:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_reg', '0004_auto_20170222_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='books',
            new_name='book',
        ),
    ]
