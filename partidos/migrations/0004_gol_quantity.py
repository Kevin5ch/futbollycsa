# Generated by Django 3.2.4 on 2022-03-03 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partidos', '0003_alter_partido_active_gol'),
    ]

    operations = [
        migrations.AddField(
            model_name='gol',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
