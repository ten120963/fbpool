# Generated by Django 3.1.4 on 2020-12-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poolapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='week',
            field=models.IntegerField(),
        ),
    ]
