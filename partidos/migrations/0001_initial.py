# Generated by Django 4.0.2 on 2022-03-02 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipos', '0001_initial'),
        ('torneo', '0004_cancha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Dia')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('status', models.CharField(choices=[('PD', 'Pendiente'), ('SP', 'Suspendido'), ('TR', 'Terminado')], max_length=2, verbose_name='Estado del partido')),
                ('alias', models.CharField(max_length=16, verbose_name='Alias')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('active', models.BooleanField(verbose_name='Activo')),
                ('local', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='equipos.equipo', verbose_name='Local')),
                ('stadium', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='torneo.cancha', verbose_name='Cancha')),
            ],
            options={
                'verbose_name': 'Partido',
                'verbose_name_plural': 'Partidos',
                'ordering': ['-date'],
            },
        ),
    ]
