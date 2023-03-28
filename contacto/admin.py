from django.contrib import admin
from .models import ContactoPrincipal


class ContactoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'coments', 'created_at')


# Register your models here.
    
admin.site.register(ContactoPrincipal, ContactoAdmin)

