from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required








# Create your views here.
@login_required(login_url='user_login')
def homepage(request, category_id=None):
    form = ProductSearchForm(request.POST or None)
    
    categories = Category.objects.all()
    
    products = Products.objects.all().order_by('-id')
    category = None
    
    #TO SET PAGINATION
    paginator = Paginator(products,3)
    page = request.GET.get('page')
    try:
        products=paginator.page(page)
    except PageNotAnInteger:
        products=paginator.page(1)
    except EmptyPage:
        products=paginator.page(paginator.num_pages)
        
    #END
        
        
    
    
    
    if request.method == 'POST':
        products = Products.objects.filter(name__icontains=form['name'].value())
    
    
    if category_id:
        products = Products.objects.all()
        
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)
        
            #TO SET PAGINATION
        paginator = Paginator(products,3)
        page = request.GET.get('page')
        try:
            products=paginator.page(page)
        except PageNotAnInteger:
            products=paginator.page(1)
        except EmptyPage:
            products=paginator.page(paginator.num_pages)
            
        #END
        
        
        
    
    context = {
        "products":products,
        "categories":categories,
        
        "category":category,
        "form":form,
        "page":page,
        
        
        
        
    }
    return render(request, 'DjangoApp/homepage.html', context)


def search_product_autocomplete(request):
    query_original = request.GET.get('term')
    search = Q(name__icontains=query_original) 
    product = Products.objects.filter(search)
    mylist= []
    mylist += [x.name for x in product]
    return JsonResponse(mylist, safe=False)



@login_required(login_url='user_login')
def view_product(request, id):
    products = Products.objects.get(id=id)
    context = {
        "products":products,
    }
    return render(request, 'DjangoApp/view_product.html', context)
@login_required(login_url='user_login')
def delete_product(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    messages.success(request, "Product Deleted Successfully")
    
    return redirect('homepage')
    
@login_required(login_url='user_login')
def add_product(request):
    form = ProductsForm()
    if request.method == "POST":
        form = ProductsForm(request.POST, files = request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Added Successfully")
            return redirect('homepage')
    context= {
        "form":form
    }
        
    
    
    return render(request, 'DjangoApp/add_product.html', context)
@login_required(login_url='user_login') 
def update_product(request, id):
    product = Products.objects.get(id=id)
    form = ProductsForm(instance=product)
    if request.method == "POST":
        form = ProductsForm(request.POST, files = request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Updated Successfully")
            
            return redirect('homepage')
    context= {
        "form":form,
        "product":product
    }
        
    
    
    return render(request, 'DjangoApp/update_product.html', context)  
    

def about(request):
    return render(request, 'DjangoApp/about.html')

def user_register(request):
    form = UserRegisterForm()
    username= request.POST.get('username')
    if request.method == "POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"{username} successfully registered")
            return redirect('homepage')
    context = {
        "form":form,
    }
    return render(request, 'DjangoApp/user_register.html',context)

def user_login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('homepage')
        else:
            messages.info(request,"Username or Password incorrect")
            return redirect('user_login')
        
    return render(request, 'DjangoApp/user_login.html')

def user_logout(request):
    auth.logout(request)
    return redirect('user_login')








