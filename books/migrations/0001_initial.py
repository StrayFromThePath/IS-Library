# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import select2.fields


class Migration(migrations.Migration):

    dependencies = [
        ('readers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookLend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('abonement1', models.BooleanField(default=False, verbose_name=b'\xd0\x90\xd0\xb1\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82 1')),
                ('abonement2', models.BooleanField(default=False, verbose_name=b'\xd0\x90\xd0\xb1\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82 2')),
                ('read_room', models.BooleanField(default=False, verbose_name=b'\xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xb7\xd0\xb0\xd0\xbb')),
                ('lend_date', models.DateField(default=datetime.datetime.now, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', editable=False)),
                ('lend_date_end', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xb2\xd1\x80\xd0\xb0\xd1\x82\xd0\xb0')),
                ('lend_date_fact', models.DateField(null=True, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xba\xd1\x82\xd0\xb8\xd1\x87\xd0\xb5\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f \xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xb2\xd1\x80\xd0\xb0\xd1\x82\xd0\xb0', blank=True)),
                ('mark_return', models.BooleanField(default=False, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb0 \xd0\xbe \xd0\xb2\xd0\xbe\xd0\xb7\xd0\xb2\xd1\x80\xd0\xb0\xd1\x82\xd0\xb5')),
            ],
            options={
                'db_table': 'book_lend',
                'verbose_name': '\u0412\u044b\u0434\u0430\u0447\u0430 \u043a\u043d\u0438\u0433\u0438',
                'verbose_name_plural': '\u0412\u044b\u0434\u0430\u0447\u0430 \u043a\u043d\u0438\u0433',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('author', models.CharField(max_length=255, verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80/\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80\xd1\x8b')),
                ('publisher', models.CharField(max_length=100, verbose_name=b'\xd0\x98\xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd1\x81\xd1\x82\xd0\xb2\xd0\xbe')),
                ('date_publ', models.CharField(max_length=4, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8\xd0\xb7\xd0\xb4\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('date_reg', models.DateField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('abonement1', models.BooleanField(default=False, verbose_name=b'\xd0\x90\xd0\xb1\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82 1')),
                ('abonement2', models.BooleanField(default=False, verbose_name=b'\xd0\x90\xd0\xb1\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82 2')),
                ('read_room', models.BooleanField(default=False, verbose_name=b'\xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xb7\xd0\xb0\xd0\xbb')),
                ('price', models.DecimalField(verbose_name=b'\xd0\xa1\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c', max_digits=7, decimal_places=2)),
                ('count_all', models.IntegerField(verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x89\xd0\xb5\xd0\xb5 \xd0\xba\xd0\xbe\xd0\xbb-\xd0\xb2\xd0\xbe')),
                ('count_in', models.IntegerField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb-\xd0\xb2\xd0\xbe \xd0\xb2 \xd0\xbd\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb8\xd0\xb8')),
                ('count_ab1', models.IntegerField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb-\xd0\xb2\xd0\xbe \xd0\xb2 \xd0\x90\xd0\xb1\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb5 1', blank=True)),
                ('count_ab2', models.IntegerField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb-\xd0\xb2\xd0\xbe \xd0\xb2 \xd0\x90\xd0\xb1\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb5 2', blank=True)),
                ('count_rr', models.IntegerField(null=True, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbb-\xd0\xb2\xd0\xbe \xd0\xb2 \xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xbe\xd0\xbc \xd0\xb7\xd0\xb0\xd0\xbb\xd0\xb5', blank=True)),
            ],
            options={
                'db_table': 'catalog',
                'verbose_name': '\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043a\u043d\u0438\u0433',
                'verbose_name_plural': '\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043a\u043d\u0438\u0433',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'db_table': 'section',
                'verbose_name': '\u0420\u0430\u0437\u0434\u0435\u043b',
                'verbose_name_plural': '\u0420\u0430\u0437\u0434\u0435\u043b\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='catalog',
            name='section',
            field=models.ForeignKey(verbose_name=b'\xd0\xa0\xd0\xb0\xd0\xb7\xd0\xb4\xd0\xb5\xd0\xbb', to='books.Section'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booklend',
            name='book',
            field=select2.fields.ForeignKey(verbose_name=b'\xd0\x9a\xd0\xbd\xd0\xb8\xd0\xb3\xd0\xb0', to='books.Catalog'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='booklend',
            name='reader',
            field=select2.fields.ForeignKey(verbose_name=b'\xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to='readers.Reader'),
            preserve_default=True,
        ),
    ]
