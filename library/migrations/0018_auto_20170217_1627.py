# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-17 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_reader_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(default=b'pic_folder/None/no-img.jpg', upload_to=b'pic_folder/')),
            ],
        ),
        migrations.AlterField(
            model_name='reader',
            name='photo',
            field=models.ImageField(blank=True, upload_to=b'media/image/'),
        ),
    ]
