from django.shortcuts import render,redirect
from .models import CustomUser
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def SignUp(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')

        my_user = CustomUser(username = name,email = email,contact_number = contact)
        my_user.set_password(password)
        my_user.save()
        return redirect('Login')

    return render(request,'signup.html')

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        print(name)
        print(password)
        nw_user = CustomUser.objects.get(username = name)
        print(nw_user.password)
        user = authenticate(request,username = name,password = password)
        print("hellloooo ")
        print(user)
        if user is not None:
            login(request,user)
            return redirect('SignUp')
    return render(request,'login.html')