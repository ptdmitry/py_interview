from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Product
from .forms import ProductForm


def index(request):
    return render(request, 'product_catalog/index.html', {'products': Product.objects.all()})


def add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
    return render(request, 'product_catalog/form.html', {'form': form})
