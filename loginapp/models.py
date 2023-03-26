from django.db import models

class usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    usuario = models.CharField(max_length=60)
    password = models.CharField(max_length=60)
    estado = models.BooleanField(default=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.usuario, self.estado)

    class Meta: db_table = 'usuario'

class informacion(models.Model):
    id = models.IntegerField(primary_key=True)
    ci = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    fcha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0} - [{1}] - [{2}]"
        return texto.format(self.usuario.usuario, self.nombre, self.usuario.estado)

    class Meta: db_table = 'informacion'