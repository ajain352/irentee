# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('irent', '0002_remove_user_registration_lname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_registration',
            name='product_photo_id',
        ),
        migrations.AddField(
            model_name='product_registration',
            name='product_photo',
            field=models.ImageField(upload_to=b'path/', verbose_name=b'img', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='ucity',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_registration',
            name='umobile',
            field=models.CharField(max_length=12, null=True),
            preserve_default=True,
        ),
    ]
