# Generated by Django 2.1.2 on 2018-12-07 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursiones', '0002_excursion_banners'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursiones',
            name='recomendado',
            field=models.BooleanField(default=False),
        ),
    ]