from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        confirm_password = request.POST['confirm_password']

        user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
        user.save()
        print('User created')
        redirect('/')
    else:
        return render(request,'register.html')