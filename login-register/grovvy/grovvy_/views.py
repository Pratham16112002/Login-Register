from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    return  render(request,'authentication/index.html')
 
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        myUser = User.objects.create_user(username,email,password1) 
        # This is the easiest way to create new users into the database
        myUser.first_name=fname
        myUser.last_name=lname
        myUser.save()
        messages.success(request,"Your accout has been successfully created .")
        return redirect('signin')
    return render(request , 'authentication/signup.html')

def signin(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password = password)

        if user is not None :
            login(request,user)
            fname = user.first_name
            return render(request,'authentication/index.html',{'fname':fname})
        else :
            messages.error(request, "Invalid Credentials")
            return redirect('index')
    return render(request , 'authentication/signin.html')
def signout(request):
    pass