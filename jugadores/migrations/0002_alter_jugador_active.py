# Generated by Django 4.0.2 on 2022-03-02 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jugadores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
