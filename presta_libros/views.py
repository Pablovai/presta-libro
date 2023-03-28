from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from nlibros.models import Product, ReviewRating
from accounts.models import Account, UserProfile
from category.models import Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib import messages


def home(request):
    novelas = Product.objects.order_by("-created_date").all()
    
    userprofile = UserProfile.objects.all()
    
    reviews = ReviewRating.objects.all().order_by("-created_at")[:3]

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(novelas, 4)
        novelas = paginator.page(page)
    except:
        raise Http404     
    
    try:
        userprofile = UserProfile.objects.get(user_id=request.user.id)
    except:
        pass


    context ={
        'novelas':novelas,
        'userprofile': userprofile,
        'paginator': paginator,
        'reviews': reviews,

    }
    
    return render(request, 'home.html', context)



def reglamento(request):
    return render(request, 'reglamento.html')





# libros=Libro.objects.order_by("autor").all()[:9] 
#    return render(request, 'home.html', {"libros": libros})
# books_count = libros.count()
#'conteo_libro':books_count,

# reviews = ReviewRating.objects.all()[:3]


    #reviews = None
    #for product in novelas:
        # reviews = ReviewRating.objects.filter(product_id=product.id, status=True)


        #if request.user.is_authenticated:
    #else:
        #return render(request, 'home.html')