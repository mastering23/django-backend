from django.http import Http404, HttpResponse
from django.shortcuts import render,get_object_or_404

from .forms import ProductoForm
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
    producto = get_object_or_404(Producto, id=producto_id)
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'detalle.html', {'producto': producto})

def formulario(request):
  form = ProductoForm()  
  return render(request,'producto_form.html',{'form': form})