# Generated by Django 2.1.2 on 2018-11-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoteles',
            name='imagen',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]