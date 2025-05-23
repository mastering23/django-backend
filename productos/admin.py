from django.contrib import admin
from .models import Categoria,Producto

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
  list_display =('id','nombre')
  
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto)