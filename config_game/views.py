from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ElementoForm, EfectoForm
from .models import Elemento, Efecto

# Vista de prueba
def index(request):
    return HttpResponse("Hello, world. You're at the configuration game index.")

# Vista que permite listar todos los registros del modelo 'Elemento'
def list_elements(request):
    elements = Elemento.objects.all()
    return render(request, 'elements.html', {'elements': elements})

# Vista que permite crear registros del modelo 'Elemento'
def create_element(request):
    form = ElementoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_elements')

    return render(request, 'elements-form.html', {'form': form})

# Vista que permite listar todos los registros del modelo 'Efecto'
def list_efects(request):
    efects = Efecto.objects.all()
    return render(request, 'efects.html', {'efects': efects})

# Vista que permite crear registros del modelo 'Efecto'
def create_efects(request):
    form = EfectoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_efects')

    return render(request, 'efects-form.html', {'form': form})

# Vista que permite modificar registros del modelo 'Efecto'
def update_efects(request, id):
    my_efect = Efecto.objects.get(id=id)
    form = EfectoForm(request.POST or None, instance=my_efect)

    if form.is_valid():
        form.save()
        return redirect('list_efects')

    return render(request, 'efects-form.html', {'form': form, 'my_efect': my_efect})

# Vista que permite eliminar registros del modelo 'Efecto'
def delete_efects(request, id):
    my_efect = Efecto.objects.get(id=id)

    if request.method == 'POST':
        my_efect.delete()
        return redirect('list_efects')

    return render(request, 'efects-delete.html', {'my_efect': my_efect})