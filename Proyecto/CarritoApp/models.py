from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField()
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'