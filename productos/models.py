from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
  nombre = models.CharField(max_length=60)
  def __str__(self):
    return self.nombre

class Producto(models.Model):
  nombre = models.CharField(max_length=60)
  stock = models.IntegerField() 
  puntaje = models.FloatField()
  # CASCADE : eliminar el producto
  # PROTECT : lanza un error 
  # RESTRICT : solo elimina si no existe productos
  # SET_null : Actuliza valor nulo
  # SET_DEFAULT:
  categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
  
  
  creado_en = models.DateField(default=timezone.now)
  
  
  def __str__(self):
    return self.nombre