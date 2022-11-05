# Generated by Django 4.1.2 on 2022-11-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0007_alter_house_pets_allowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='price_per_night',
            field=models.PositiveIntegerField(help_text='Positive Numbers Only', verbose_name='Price'),
        ),
    ]
