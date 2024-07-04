from django.shortcuts import render, redirect
from . models import Medicine

# Create your views here.


def add_item(request):
    if request.method == 'POST':
        name = request.POST['name']
        # category = request.POST['category']
        quantity = request.POST['quantity']
        price = request.POST['price']

        new_med = Medicine(name=name, quantity=quantity, price=price)
        new_med.save()
        return redirect('products')
    
    return render(request, 'add_med.html')




def about(request):
    return render(request, 'about.html')

def register(request):
    return render(request, 'register.html')


def products(request):
    medicine = Medicine.objects.all()
    return render(request, 'products.html', {"medicine":medicine})



def home(request):
    return render(request, 'index.html')


def login_user(request):
    return render(request, 'login.html')