# Generated by Django 2.1.2 on 2018-12-10 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0011_auto_20181210_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotele',
            name='capacidad_habitacion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='hotele',
            name='costo',
            field=models.CharField(max_length=50),
        ),
    ]