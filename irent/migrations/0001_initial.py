# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('pc_id', models.AutoField(serialize=False, primary_key=True)),
                ('pc_name', models.CharField(max_length=70)),
            ],
            options={
                'db_table': 'product_category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product_registration',
            fields=[
                ('uid', models.IntegerField()),
                ('product_id', models.AutoField(serialize=False, primary_key=True)),
                ('product_name', models.CharField(max_length=30)),
                ('pc_id', models.IntegerField()),
                ('product_title', models.CharField(max_length=100)),
                ('product_description', models.CharField(max_length=500)),
                ('rental_condition', models.CharField(max_length=500)),
                ('product_photo_id', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'product_registration',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(serialize=False, primary_key=True)),
                ('umail', models.EmailField(unique=True, max_length=30)),
                ('upass', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User_registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.IntegerField()),
                ('uname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('umobile', models.CharField(max_length=12)),
                ('ucity', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'users_registration',
            },
            bases=(models.Model,),
        ),
    ]
