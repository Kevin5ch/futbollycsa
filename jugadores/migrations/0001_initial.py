# Generated by Django 3.2.5 on 2022-02-28 23:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=16, verbose_name='Apellido')),
                ('email', models.CharField(max_length=64, verbose_name='Email')),
                ('alias', models.CharField(max_length=16, verbose_name='Alias')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('active', models.BooleanField(verbose_name='Activo')),
                ('equipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipos.equipo')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
                'ordering': ['-name'],
            },
        ),
    ]
