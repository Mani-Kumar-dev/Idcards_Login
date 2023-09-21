from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from Card_Id.models import Virtual_Id
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
def virtual_Id(request,Name):
    allPosts=get_object_or_404(Virtual_Id, Name=Name.upper())
    # print(allPosts)
    context={'allPosts':allPosts}
    return render (request,'index.html',context)

def SignIn(request):
        if request.method == "POST":
            
            UserName = request.POST.get('UserName')
            Email = request.POST.get('Email')
            Password = request.POST.get('Pass')
            Cpassword = request.POST.get('Cpass')

            if Password != Cpassword:
                messages.info(request,"Do not MatchPassword")
                return redirect("/")
            try:
                if User.objects.get( UserName =  UserName):
                    messages.info(request,"Alreday Used Username Try New")
                    return redirect("/")
            except Exception as identifier:
                pass
            try:
                 if User.objects.get(Email = Email):
                    messages.info(request,"Used Email Try New")
                    return redirect("/")
            except Exception as identifier:
                pass
            myuser=User.objects.create_user( Email,UserName,Password)
            myuser.save()
            messages.info(request,"Successfully Signed")
            return redirect("/profile_login")
        
        return render(request,'signIn.html')
def LogIn(request):
    if request.method == "POST":
        UserNameLog=request.POST.get('UserNameLog')
        PasswordLog=request.POST.get('PasswordLog')
        username = User.objects.get(username = UserNameLog)
        # password = User.objects.get(password = PasswordLog)
        print(username)
        # print(password)

        myuser=authenticate(username=username,password=PasswordLog)
    
        print(myuser)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Successfully')
            return redirect(f'/virtual_Id/{username}')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/profile_login')

    return render(request,"login.html")