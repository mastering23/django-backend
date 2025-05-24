from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto

# Create your views here.
def index(request):
  productos  = Producto.objects.all()
  
  return render(
    request,
    'index.html',
    context={'productos': productos}
  )


def detalle(request, producto_id):
    return HttpResponse(f"Producto ID: {producto_id}")