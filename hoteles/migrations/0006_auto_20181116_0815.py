# Generated by Django 2.1.2 on 2018-11-16 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0005_auto_20181116_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotele',
            name='costo',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
