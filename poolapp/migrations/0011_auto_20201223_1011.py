# Generated by Django 3.1.4 on 2020-12-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poolapp', '0010_auto_20201219_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.TextField(),
        ),
    ]