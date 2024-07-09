from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('products/', views.products, name="products"),
    path('register/', views.register, name="register"),
    path('about/', views.about, name="about"),

    path('add_item/', views.add_item, name="add_item"),
    path('logout/', views.logout_user, name="logout"),
]
