# Generated by Django 3.2.5 on 2022-02-28 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='Nombre')),
                ('alias', models.CharField(max_length=16, verbose_name='Alias')),
                ('logo', models.ImageField(default='null', upload_to='equipos')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('active', models.BooleanField(verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['-name'],
            },
        ),
    ]
