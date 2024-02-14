# Generated by Django 5.0 on 2024-01-24 21:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id_carta', models.AutoField(primary_key=True, serialize=False)),
                ('pedido', models.CharField(max_length=40)),
                ('folio', models.CharField(max_length=40)),
                ('origen', models.CharField(max_length=40)),
                ('destino', models.CharField(max_length=40)),
                ('maniobras', models.CharField(max_length=40)),
                ('diesel', models.CharField(max_length=40)),
                ('gastos', models.CharField(max_length=40)),
                ('hora_reporte', models.DateTimeField()),
                ('inicio_carga', models.DateTimeField()),
                ('termino_carga', models.DateTimeField()),
                ('inicio_ruta', models.DateTimeField()),
                ('arribo_cliente', models.DateTimeField()),
                ('inicio_descarga', models.DateTimeField()),
                ('termino_descarga', models.DateTimeField()),
                ('termino_viaje', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('carta', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='administrador.registro')),
            ],
        ),
    ]
