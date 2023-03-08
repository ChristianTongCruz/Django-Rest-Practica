from django.db import models

# Create your models here.
# The class DatosGenerales is a model that has the following fields: id_datos_generales,
# lugar_nacimiento, sexo, edad, estado_civil, residencia_permanente_vivienda, numero_piso_vivienda
class DatosGenerales(models.Model):
    id_datos_generales = models.AutoField(primary_key=True)
    lugar_nacimiento = models.CharField(max_length=45)
    sexo = models.CharField(max_length=1)
    edad = models.IntegerField()
    estado_civil = models.CharField(max_length=45)
    residencia_permanente_vivienda = models.CharField(max_length=2)
    numero_piso_vivienda = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'datos_generales'