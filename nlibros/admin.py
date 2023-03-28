from django.contrib import admin
from .models import Product, ReviewRating

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('autor', 'product_name', 'estado_libro', 'genero_libro', 'puntuacion', 'created_date', 'modified_date')
    prepopulated_fields = {'slug' : ('product_name',)}



class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'rating', 'subject', 'created_at')


admin.site.register(Product, ProductAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)


