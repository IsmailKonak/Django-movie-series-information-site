from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewUserForm
from .models import NewUser
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls import reverse

def logout_view(request):
    logout(request)
    # Redirect to a success page.
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST or None,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, ('Your registiration has been submitted successfully!'))
            user_db = NewUser.objects.all()
            last_user = user_db.last()
            
            return render(request, "registration/login.html",{
                    "username":last_user,
                })
        else:
            print(form)
            messages.success(request, ('ERROR!'))
            r = request.POST
            username = r.get("username")
            fname = r.get("fname")
            lname = r.get("lname")
            email = r.get("email")
            birthday = r.get("birthday")
            twitter = r.get("twitter")
            instagram = r.get("instagram")
            facebook = r.get("facebook")
            return render(request, "registration/register.html",{
                "username": username,
                "fname": fname,
                "lname": lname,
                "email": email,
                "birthday": birthday,
                "twitter": twitter,
                "instagram": instagram,
                "facebook": facebook,
            })
    else:
        return render(request, "registration/register.html",{})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        userlogged = authenticate(request, username=username, password=password)
        print(type(userlogged))
        if userlogged is not None:
            auth_login(request,userlogged)
            messages.success(request, ('Your loged in successfully!'))
            return redirect('profile',username=userlogged)
            ...
        else:
            messages.success(request, ('Email or the password is false'))
            return redirect('login')
            ...
    else:
        return render(request, "registration/login.html",{})

def logout_view(request):
    logout(request)
    return render(request, "registration/login.html",{})
