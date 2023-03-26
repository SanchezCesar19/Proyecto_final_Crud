from django.db import models

# Create your models here.
class proveedor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        texto = "({0}) {1} [{2}] -{3}-}"
        return texto.format(self.id, self.nombre, self.direccion, self.direccion)

    class Meta: db_table = 'proveedor'


class producto(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    proveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)

    def __str__(self):
        texto = "({0}) {1} [{2}] -{3}-}"
        return texto.format(self.id, self.nombre, self.precio, self.estado)

    class Meta: db_table = 'producto'