# Generated by Django 2.2.7 on 2020-02-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamestore', '0003_game_developer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='price',
            field=models.FloatField(),
        ),
    ]
