from django import forms
from .models import ReviewRating, Product

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']




class ClienteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['autor', 'product_name', 'descripcion', 'slug', 'photo_libro',
                'estado_libro', 'genero_libro', 'puntuacion', 'tiempo_devolucion', 'cantidad_paginas',
                'unidades_disponibles', 'category' ]
