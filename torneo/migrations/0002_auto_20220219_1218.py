# Generated by Django 3.2.4 on 2022-02-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temporada',
            options={'ordering': ['-id'], 'verbose_name': 'Temporada', 'verbose_name_plural': 'Temporadas'},
        ),
        migrations.AddField(
            model_name='temporada',
            name='logo',
            field=models.ImageField(default='null', upload_to=''),
        ),
    ]
