# Generated by Django 3.1.4 on 2020-12-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poolapp', '0011_auto_20201223_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.TextField(default='IN'),
        ),
    ]
