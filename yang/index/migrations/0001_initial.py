# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('upwd', models.CharField(max_length=18)),
                ('uname', models.CharField(max_length=14)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='wenjian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('wenjian', models.CharField(max_length=20)),
                ('lujing', models.CharField(max_length=60)),
                ('uname', models.CharField(max_length=14)),
                ('gxname', models.CharField(max_length=1)),
            ],
        ),
    ]
