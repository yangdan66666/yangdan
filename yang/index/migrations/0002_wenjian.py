# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='wenjian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('wenjian', models.CharField(max_length=20)),
                ('lujing', models.CharField(max_length=50)),
                ('uname', models.CharField(max_length=14)),
                ('gxname', models.CharField(max_length=14)),
            ],
        ),
    ]
