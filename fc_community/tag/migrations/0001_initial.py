# Generated by Django 3.1.1 on 2021-01-14 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='태그명')),
                ('register_dttm', models.DateField(auto_now_add=True, verbose_name='등록시간')),
            ],
            options={
                'verbose_name': '패스트캠퍼스 태그',
                'verbose_name_plural': '패스트캠퍼스 태그',
                'db_table': 'fastcampus_tag',
            },
        ),
    ]
