# Generated by Django 2.1.2 on 2018-12-10 18:26

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excursiones', '0005_auto_20181210_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'imagen',
                'verbose_name_plural': 'Slider detalle',
            },
        ),
        migrations.AlterField(
            model_name='excursiones',
            name='costo',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='excursiones',
            name='itinerario',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AddField(
            model_name='imagenes',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='images', to='excursiones.excursiones'),
        ),
    ]
