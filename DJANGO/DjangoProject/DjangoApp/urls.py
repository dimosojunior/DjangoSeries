
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('<int:category_id>/', views.homepage, name="product_by_category"),
    
    path('about/', views.about, name="about"),
    path('view_product/<int:id>/', views.view_product, name="view_product"),
    path('delete_product/<int:id>/', views.delete_product, name="delete_product"),
    path('add_product/', views.add_product, name="add_product"),
    path('update_product/<int:id>/', views.update_product, name="update_product"),
    path('search_product_autocomplete/', views.search_product_autocomplete, name="search_product_autocomplete"),
    path('user_register/', views.user_register, name="user_register"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    
    
    
]