# Generated by Django 4.0.2 on 2022-03-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0004_cancha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancha',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='temporada',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
    ]
