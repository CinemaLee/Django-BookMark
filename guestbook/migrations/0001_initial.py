# Generated by Django 2.2.3 on 2019-07-16 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('passwd', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('post_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
