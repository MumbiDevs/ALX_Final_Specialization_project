from django.shortcuts import render, redirect
from . models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You are now Logged in Successfully!!!"))
            return redirect('home')
        else:
            messages.success(request,("There was an Error. Please try Again!"))
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
   logout(request)
   messages.success(request, ("You have been logged out!!!"))
   return redirect ('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save the user instance
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            
            # Authenticate and log in the user
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have registered successfully!")
                return redirect('home')
            else:
                messages.error(request, "Authentication failed after registration. Please try logging in.")
                return redirect('login')  # Redirect to login page if login fails
        else:
            # Display form errors to the user
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = SignUpForm()

    # Render the registration page
    return render(request, 'register.html', {'form': form})

def category(request, foo):
    # Replace hyphens with spaces
    foo = foo.replace('-', ' ')
    
    try:
        # Look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'categories.html', {'products': products, 'category': category}) 
    except:
        messages.error(request, "That category does not exist!")
        return redirect('home')