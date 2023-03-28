from category.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count

# Create your models here.


class RangeIntegerField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        validators = kwargs.pop("validators", [])
        
        # turn min_value and max_value params into validators
        min_value = kwargs.pop("min_value", None)
        if min_value is not None:
            validators.append(MinValueValidator(min_value))
        max_value = kwargs.pop("max_value", None)
        if max_value is not None:
            validators.append(MaxValueValidator(max_value))

        kwargs["validators"] = validators

        super().__init__(*args, **kwargs)



class Product(models.Model):
    
    deterioro_libro=(
        ('Malo','Malo'),
        ('Regular','Regular'),
        ('Bueno','Bueno'),
        ('Muy_bueno','Muy Bueno'),
        ('Excelente','Excelente'),
        
    )
    
    autor = models.CharField(max_length=100, blank=True)
    product_name = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250)
    slug = models.CharField(max_length=100, unique=True)
    photo_libro = models.ImageField(upload_to='photos/%Y/%m/%d/')
    estado_libro = models.CharField(choices=deterioro_libro, max_length=100)
    genero_libro = models.CharField(max_length=100)
    puntuacion = models.FloatField(blank=True)
    tiempo_devolucion = models.CharField(max_length=110, blank=True)
    cantidad_paginas = models.IntegerField(blank=True) 
    unidades_disponibles = models.IntegerField(blank=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    def __str__(self):
        return self.product_name
    
    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg=0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg
    
    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count=0
        if reviews['count'] is not None:
            count = int(reviews['count'])

        return count
    


class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.CharField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
        


