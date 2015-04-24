# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f')),
                ('secondname', models.CharField(max_length=20, verbose_name=b'\xd0\x9e\xd1\x82\xd1\x87\xd0\xb5\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe')),
                ('lastname', models.CharField(max_length=40, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xbc\xd0\xb8\xd0\xbb\xd0\xb8\xd1\x8f')),
                ('date_add', models.DateField(default=datetime.datetime(2015, 4, 23, 1, 45, 37, 962000), verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb8 \xd0\xb2 \xd0\xb1\xd0\xb8\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xbe\xd1\x82\xd0\xb5\xd0\xba\xd1\x83')),
                ('date_del', models.DateField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xb1\xd0\xb8\xd1\x82\xd0\xb8\xd1\x8f \xd0\xb8\xd0\xb7 \xd0\xb1\xd0\xb8\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xbe\xd1\x82\xd0\xb5\xd0\xba\xd0\xb8', blank=True)),
                ('right_read_rom', models.BooleanField(default=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbe \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f \xd1\x87\xd0\xb8\xd1\x82\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xbc \xd0\xb7\xd0\xb0\xd0\xbb\xd0\xbe\xd0\xbc')),
                ('right_abonement', models.BooleanField(default=True, verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd0\xbb\xd0\xbe \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c\xd1\x81\xd1\x8f \xd0\xb0\xd0\xb1\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xbe\xd0\xbc')),
            ],
            options={
                'db_table': 'reader',
                'verbose_name': '\u0427\u0438\u0442\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u0427\u0438\u0442\u0430\u0442\u0435\u043b\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OnceOnly',
            fields=[
                ('reader_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='readers.Reader')),
                ('phone', models.CharField(max_length=20, verbose_name=b'\xd0\x9d\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0')),
            ],
            options={
                'db_table': 'onceonly',
                'verbose_name': '\u0420\u0430\u0437\u043e\u0432\u044b\u0439 \u0447\u0438\u0442\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u0420\u0430\u0437\u043e\u0432\u044b\u0435 \u0447\u0438\u0442\u0430\u0442\u0435\u043b\u0438',
            },
            bases=('readers.reader',),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('reader_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='readers.Reader')),
                ('chair', models.CharField(max_length=50, verbose_name=b'\xd0\x9a\xd0\xb0\xd1\x84\xd0\xb5\xd0\xb4\xd1\x80\xd0\xb0')),
                ('degree', models.CharField(max_length=50, null=True, verbose_name=b'\xd0\xa1\xd1\x82\xd0\xb5\xd0\xbf\xd0\xb5\xd0\xbd\xd1\x8c, \xd0\x97\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
            ],
            options={
                'db_table': 'staff',
                'verbose_name': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a',
                'verbose_name_plural': '\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438',
            },
            bases=('readers.reader',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('reader_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='readers.Reader')),
                ('group', models.CharField(max_length=20, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb3\xd1\x80\xd1\x83\xd0\xbf\xd0\xbf\xd1\x8b')),
                ('faculty', models.CharField(max_length=50, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x83\xd0\xbb\xd1\x8c\xd1\x82\xd0\xb5\xd1\x82')),
            ],
            options={
                'db_table': 'student',
                'verbose_name': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442',
                'verbose_name_plural': '\u0421\u0442\u0443\u0434\u0435\u043d\u0442\u044b',
            },
            bases=('readers.reader',),
        ),
    ]
