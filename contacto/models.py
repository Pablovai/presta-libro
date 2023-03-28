from django.db import models


# Create your models here.

class ContactoPrincipal(models.Model):
    
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    coments = models.CharField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


