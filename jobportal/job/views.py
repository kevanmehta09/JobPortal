from django.shortcuts import render,redirect,get_object_or_404
from .models import CustomUser,Company,Job
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

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
        user = authenticate(request,username = name,password = password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('Home')
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
        return redirect('Home')
    return render(request,'register_company.html')

@login_required
def Home(request):
    user = request.user
    company = Company.objects.get(user = user)
    jobs = Job.objects.all()
    paginator = Paginator(jobs, 5) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{
        # 'jobs':jobs,
        'user_company':company,
        'user':user,
        "page_obj": page_obj
    })

@login_required
def CreateJob(request):
    user_company = Company.objects.get(user=request.user)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        tags = request.POST.get('tags')
        salary = request.POST.get('salary')
        job = Job(title = title,description = description,salary = salary,company = user_company,location = location)
        # job.set_tags(tags)
        job.save()
        messages.success(request, "Job created successfully!")
        return redirect('Home')

    return render(request, 'createjob.html')

@login_required
def UpdateJob(request,jobid):
    job = get_object_or_404(Job,id=jobid)
    if request.method == 'GET':
        return render(request,'updatejob.html',{
            'job':job
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        location = request.POST.get('location')
        # tags = request.POST.get('tags')
        salary = request.POST.get('salary')
        job.title = title
        job.description = description
        job.location = location
        job.salary = salary
        # job.set_tags(tags)
        job.save()
        messages.success(request, "Job updated successfully!")
        return redirect('Home')

@login_required
def DeleteJob(request,jobid):
    job = get_object_or_404(Job,id=jobid)
    job.delete()
    messages.success(request, "Job deleted successfully!")
    return redirect('Home')

@login_required
def Logout(request):
    logout(request)
    return redirect('Login')