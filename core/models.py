from django.db import models
from unidecode import unidecode

class ContratoPlan(models.Model):
    plan = models.CharField(max_length=100)
    precio = models.IntegerField()
    rut = models.CharField(max_length=12)
    nombre_completo = models.CharField(max_length=100)
    email = models.EmailField()
    sexo = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    metodo_pago = models.CharField(max_length=50)
    fecha_contratacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_completo} - {self.plan}"


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    dia = models.CharField(max_length=20)  # Ej: 'Lunes'
    hora = models.TimeField()              # Ej: '18:00'
    profesor = models.CharField(max_length=100, blank=True)
    duracion_minutos = models.IntegerField(default=60)

    def save(self, *args, **kwargs):
        if self.dia:
            self.dia = unidecode(self.dia.strip()).lower()  # quitar tildes y pasar a minúscula
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.dia} {self.hora}"
