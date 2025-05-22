from django.db import models

# Create your models here.
class Categoria(models.Model):
  nombre = models.CharField(max_length=60)

class Producto(models.Model):
  nombre = models.CharField(max_length=60)
  stock = models.IntegerField()
  puntaje = models.FloatField()
  # CASCADE : eliminar el producto
  # PROTECT : lanza un error 
  # RESTRICT : solo elimina si no existe productos
  # SET_null : Actuliza valor nulo
  # SET_DEFAULT:
  Categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
  