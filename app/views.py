from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect 
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
    
        if password != re_password:
            messages.error(request, "Passwords do not match!")
            return redirect('index')
            
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('index')
            
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use!")
            return redirect('index')
            
        else:
            User.objects.create_user(username=username, email=email, password=password)
            
            messages.success(request, "Registered Successfully!")
            
            return redirect('login')

    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
        
        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('login')
        
    return render(request, 'login.html')
