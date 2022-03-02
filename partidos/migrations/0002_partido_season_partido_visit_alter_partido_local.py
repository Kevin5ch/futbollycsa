# Generated by Django 4.0.2 on 2022-03-02 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0004_cancha'),
        ('equipos', '0001_initial'),
        ('partidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partido',
            name='season',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='torneo.temporada', verbose_name='Temporada'),
        ),
        migrations.AddField(
            model_name='partido',
            name='visit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visit_team', to='equipos.equipo', verbose_name='Visitante'),
        ),
        migrations.AlterField(
            model_name='partido',
            name='local',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='local_team', to='equipos.equipo', verbose_name='Local'),
        ),
    ]