from django.shortcuts import render, redirect
from . models import Medicine, Category
from django.contrib import messages
from . forms import MedicineForm

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
    return render(request, 'login.html')