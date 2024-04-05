from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    #cada vez que queramos categoria retornara directamente el name
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products') # SI ELIMINAMOS UNA CATEGORIA PODEMOS DEFINIRLO COMO NULL
    is_active = models.BooleanField(default = True)
    #cada vez que queramos el product retornara directamente el name
    def __str__(self):
        return self.name
    
    @property
    def category_name(self):
        return self.category.name
    

    