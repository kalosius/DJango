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


    path('view_item/<id>', views.view_item, name="view_item"),

    path('search_item/', views.search_item, name="search_item"),
    path('edit_item/<id>', views.edit_item, name="edit_item"),
    
    path('delete/<id>', views.delete_item, name="delete")

]
