from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductsForm(forms.ModelForm):
    	
    class Meta:
        model = Products
        fields = '__all__'
        #fields =['name', 'price', 'brand']
        
class UpdateProductsForm(forms.ModelForm):
    	
    class Meta:
        model = Products
        fields = '__all__'
        #fields =['name', 'price', 'brand']
        
class ProductSearchForm(forms.ModelForm):
    name=forms.CharField(

        widget = forms.TextInput(attrs={'placeholder':'Product Name', 'id':'search'})

    )


    class Meta:
        model = Products
        fields = ["name"]
        
class UserRegisterForm(UserCreationForm):
    email = forms.CharField(max_length=50)
    	
    class Meta:
        model = User
        #fields = '__all__'
        fields =['username', 'email', 'password1','password2']
        
        
