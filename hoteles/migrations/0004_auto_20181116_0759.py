# Generated by Django 2.1.2 on 2018-11-16 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0003_auto_20181116_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotele',
            name='costo',
            field=models.DecimalField(decimal_places=6, max_digits=6),
        ),
    ]
