# Generated by Django 3.1.7 on 2021-03-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EQUIPOS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Equipo', models.TextField(max_length=120)),
                ('Jugadores', models.IntegerField()),
                ('EdadMedia', models.IntegerField()),
                ('ValorTotal', models.FloatField()),
                ('ValorMedio', models.FloatField()),
                ('Actualizacion', models.TextField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.TextField(max_length=120)),
                ('edad', models.IntegerField()),
                ('pais', models.TextField(max_length=120)),
                ('equipos', models.TextField(max_length=120)),
                ('dorsal', models.IntegerField()),
                ('posicion', models.TextField(max_length=120)),
                ('precio', models.FloatField()),
                ('actualizacion', models.TextField(max_length=120)),
            ],
        ),
    ]
