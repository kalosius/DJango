from django.shortcuts import render
from . models import Medicine

# Create your views here.


def add_item(request):
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