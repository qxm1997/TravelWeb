# Generated by Django 2.2.1 on 2020-03-15 10:46

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='add_times',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 15, 10, 46, 22, 103965), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='内容'),
        ),
    ]