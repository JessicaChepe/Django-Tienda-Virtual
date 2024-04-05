from django.shortcuts import render
# from django.http import HttpResponse
# # Create your views here.
# def hello(request):
#     return HttpResponse('<h1>Hello World</h1>')

#cuando no se encuentre el objeto pueda mostrar un error 404
from django.shortcuts import get_object_or_404, redirect
from django.http import Http404


from shop.Carrito import Carrito

from .models import *

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = { #diccionario
        'categories' : categories,
        'products' : products
    }
    return render(request, 'shop/index.html',   context)

def product_detail(request, pk):
    # product = get_object_or_404(Product, pk=pk) #Product.objects.get(id=pk)
    # context = {
    #     'product' : product
    # }
    # return render(request, 'shop/product_detail.html',context)
    try:
        product = get_object_or_404(Product, pk=pk)
        context = {
            'product': product
        }
        return render(request, 'shop/product_detail.html', context)
    except Http404:
        # Manejar el error 404 de manera personalizada
        return render(request, 'shop/Error404.html')

def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        category = Category.objects.get(id=category)
        product = Product.objects.create(
            name = name,
            description = description,
            price = price,
            category = category
        )
        return redirect('shop:product_detail', pk = product.id)
    context = {
        'categories' : Category.objects.all
    }
    return render(request, 'shop/product_create.html',context)

def tienda(request):
    products = Product.objects.all()
    return render(request,"shop/index.html", {'products' : products})


def add_product(request, product_id):
    carrito = Carrito(request)
    product = Product.objects.get(id=product_id)
    carrito.add(product)
    return redirect('shop:index')  # En add_product

def delete_product(request, product_id):
    carrito = Carrito(request)
    product = Product.objects.get(id=product_id)
    carrito.delete(product)
    return redirect('shop:index')

def subtract_product(request, product_id):
    carrito = Carrito(request)
    product = Product.objects.get(id=product_id)
    carrito.subtract(product)
    return redirect('shop:index')

def clear_card(request):
    carrito = Carrito(request)
    carrito.clear()
    return redirect('shop:index')

