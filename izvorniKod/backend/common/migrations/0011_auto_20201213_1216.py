# Generated by Django 3.1.2 on 2020-12-13 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20201211_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laundry',
            name='pause_end',
            field=models.TimeField(blank=True, null=True),
        ),
    ]