# Generated by Django 3.2.5 on 2022-02-28 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0003_alter_temporada_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nombre de la cancha')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('active', models.BooleanField(verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Cancha',
                'verbose_name_plural': 'Canchas',
                'ordering': ['-name'],
            },
        ),
    ]
