# Generated by Django 2.1.2 on 2018-12-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home_banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripción', models.TextField()),
                ('imagen', models.ImageField(upload_to='home/banners', verbose_name='Imagen')),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualizacion')),
            ],
            options={
                'verbose_name': 'home_banners',
                'verbose_name_plural': 'home_banners',
                'ordering': ['-creacion'],
            },
        ),
    ]
