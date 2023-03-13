from django.db import models
import datetime

# Create your models here.

class MenuItem(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    img = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.nome

class Category(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class OrderModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)  
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)

    def __str__(self):
        return f'Order: {self.created.strftime("%b %d %I: %M %p")}'