# Generated by Django 3.1.1 on 2020-11-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0002_auto_20201117_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataprovider',
            name='port',
            field=models.PositiveIntegerField(default=502),
        ),
    ]
