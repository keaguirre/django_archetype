from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, verbose_name="ID Producto")
    nombre = models.CharField(max_length=255, verbose_name="Nombre del Producto", blank=False)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.IntegerField(verbose_name="Precio del Producto", blank=False, null=False)
    imagen = models.URLField(max_length=255, verbose_name="URL de la Imagen", blank=True, null=True)
    stock = models.PositiveIntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
