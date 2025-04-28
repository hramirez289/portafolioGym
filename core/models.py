from django.db import models

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
