# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0002_auto_20190414_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('atitle', models.CharField(max_length=20)),
                ('aParent', models.ForeignKey(blank=True, null=True, to='booktest.AreaInfo')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeBasicInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField(default=False)),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeDetailInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('addr', models.CharField(max_length=256)),
                ('tel', models.CharField(max_length=13)),
                ('employee_basic', models.OneToOneField(to='booktest.EmployeeBasicInfo')),
            ],
        ),
        migrations.CreateModel(
            name='NewsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='newsinfo',
            name='news_type',
            field=models.ManyToManyField(to='booktest.NewsType'),
        ),
    ]
