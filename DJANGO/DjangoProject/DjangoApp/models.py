from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('product_by_category', args=[self.id])


class Products(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = RichTextUploadingField(blank=True, null=True)
    
    brand = models.CharField(max_length=50, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to="media/")
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    ordered=models.BooleanField(default=False)
    quantity= models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)
    ordered_date=models.BooleanField()
    
    
    def __str__(self):
        return self.user.username
