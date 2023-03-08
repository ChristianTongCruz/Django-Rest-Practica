# Generated by Django 4.1.7 on 2023-03-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosGenerales',
            fields=[
                ('id_datos_generales', models.AutoField(primary_key=True, serialize=False)),
                ('lugar_nacimiento', models.CharField(max_length=45)),
                ('sexo', models.CharField(max_length=1)),
                ('edad', models.IntegerField()),
                ('estado_civil', models.CharField(max_length=45)),
                ('residencia_permanente_vivienda', models.CharField(max_length=2)),
                ('numero_piso_vivienda', models.IntegerField()),
            ],
            options={
                'db_table': 'datos_generales',
                'managed': False,
            },
        ),
    ]
