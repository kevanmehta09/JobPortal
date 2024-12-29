from django.shortcuts import render,redirect
from .models import CustomUser,Company
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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
        login(request,my_user)
        return redirect('CompanyRegister')

    return render(request,'signup.html')

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        nw_user = CustomUser.objects.get(username = name)
        user = authenticate(request,username = name,password = password)
        if user is not None:
            login(request,user)
            return redirect('SignUp')
    return render(request,'login.html')

@login_required
def CompanyRegister(request):
    print(request.user)
    if request.method == 'POST':
        cname = request.POST.get('cname')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        user = request.user

        company = Company(user = user,name = cname, address = address, contact_number = contact)
        company.save()
        return redirect('Login')
    return render(request,'register_company.html')