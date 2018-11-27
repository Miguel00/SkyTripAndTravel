# Generated by Django 2.1.2 on 2018-11-18 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0006_auto_20181116_0815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hotele',
            options={'ordering': ['-creacion'], 'verbose_name': 'Hoteles', 'verbose_name_plural': 'Hoteles'},
        ),
        migrations.AlterField(
            model_name='hotele',
            name='actualizacion',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion'),
        ),
        migrations.AlterField(
            model_name='hotele',
            name='creacion',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
        migrations.AlterField(
            model_name='hotele',
            name='imagen',
            field=models.ImageField(upload_to='hoteles', verbose_name='Imagen'),
        ),
    ]
