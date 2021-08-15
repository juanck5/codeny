from django.db import models

# Create your models here.
class periodo(models.Model):
    codigo = models.IntegerField(primary_key=True , default="999")
    Fecha_inicio = models.DateField(default="")
    Fecha_final = models.DateField(default="")