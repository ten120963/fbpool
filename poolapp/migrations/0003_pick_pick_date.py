# Generated by Django 3.1.4 on 2020-12-10 00:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('poolapp', '0002_auto_20201209_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='pick',
            name='pick_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
