from django.shortcuts import render, redirect
from . models import Medicine, Category
from django.contrib import messages
from . forms import MedicineForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.


def add_item(request):
    form = MedicineForm()
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Added Successfully!!!")
            return redirect('products')
        else:
            messages.success(request, "Invalid Input!!!")
            return redirect('add_item')

    return render(request, 'add_med.html', {"form":form})


    # html logic
    # if request.method == 'POST':
    #     name = request.POST['name']
    #     # category = request.POST['category']
    #     quantity = request.POST['quantity']
    #     price = request.POST['price']

    
    #     new_med = Medicine(name=name, quantity=quantity, price=price)
    #     new_med.save()
    #     messages.success(request, 'Item Added Successfully!')
    #     return redirect('products')
    
    # return render(request, 'add_med.html')




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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome Back {username}!')

            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password!')
            return redirect('login')    
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been Logged out Successfully!')
    return redirect('home')
    