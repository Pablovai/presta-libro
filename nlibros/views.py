from ast import keyword
from this import d
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ReviewRating
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm, ClienteForm
from django.contrib import messages


# Create your views here.
@login_required(login_url='login')
def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None: 
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True).order_by("autor")
        books_count = products.count()

    else:
        products=Product.objects.all().filter(is_available=True).order_by("autor")
        books_count = products.count()
        
    
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(products, 4)
        products = paginator.page(page)
    except:
        raise Http404     
    
    

    
    context ={
        'products':products,
        'conteo_libro':books_count,
        'paginator': paginator
    }

    return render(request, 'nlibros/nlibros.html', context)



@login_required(login_url='login')
def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    
    reviews = ReviewRating.objects.filter(product_id=single_product.id, status=True)

    context = {
        'single_product': single_product,
        'reviews': reviews,

    }
    return render(request, 'nlibros/product_detail.html', context)



@login_required(login_url='login')
def search(request):
    products = None
    books_count = None

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products=Product.objects.order_by("autor").filter(Q(product_name__icontains=keyword) | Q(autor__icontains=keyword) )
            books_count = products.count()
    
    context = {
        'products':products,
        'conteo_libro':books_count
    }        
    
    return render(request, 'nlibros/nlibros.html', context)


            
def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Muchas gracias!, tu comentario ha sido actualizado')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Muchas gracias, tu comentario fue enviado con exito!')
                return redirect(url)
    return redirect(url)



def cargar_libro(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        
        if form.is_valid():
                data = Product()
                data.autor = form.cleaned_data['TXTautor']
                data.product_name = form.cleaned_data['TXTproduct_name']
                data.descripcion = form.cleaned_data['TXTdescripcion']
                data.slug = form.cleaned_data['TXTslug']
                data.photo_libro = form.cleaned_data['TXTphoto_libro']
                data.estado_libro = form.cleaned_data['TXTestado_libro']
                data.genero_libro = form.cleaned_data['TXTgenero_libro']
                data.puntuacion = form.cleaned_data['TXTpuntuacion']
                data.tiempo_devolucion = form.cleaned_data['TXTtiempo_devolucion']
                data.cantidad_paginas = form.cleaned_data['TXTcantidad_paginas']
                data.unidades_disponibles = form.cleaned_data['TXTunidades_disponibles']
                data.category = form.cleaned_data['TXTcategory']

                data.save()
                messages.success(request, 'Muchas gracias, tu comentario fue enviado con exito!')
        else:
            print("no ves que no anda esta mierda")

    else:
        form = ClienteForm()       
                            
    return render(request, 'nlibros/cargar_libro.html', {'form':form})





    

    


