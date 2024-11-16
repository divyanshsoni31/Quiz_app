from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib import messages
from .models import question,result
from django.contrib.auth.decorators import login_required
# Create your views here.

def landing(request):
    return render(request,"welcome.html")


@login_required(login_url='login')
def index(request):
    questions = question.objects.all()
    if request.method == "POST":
        score = 0
        for ques in questions:
            selected_option = request.POST.get(str(ques.id))
            if selected_option and int(selected_option) == ques.correct_option:
                score+=1
        result.objects.update_or_create(
            user=request.user,  
            defaults={"marks": score}
        )
        return redirect("marks")
    return render(request,"Quiz.html",{"ques":questions})


@login_required(login_url='login')
def score(request):
    score = result.objects.get(user=request.user).marks
    return render(request,"marks.html",{"marks":score})

def loginview(request):
    if request.method == "POST":
        username = request.POST["username"]
        password= request.POST["password"]
        
        validate_user = authenticate(username=username,password=password)
        if validate_user is not None:
            auth_login(request,validate_user)
            print("user authenticated",validate_user)
            return redirect("quiz")
        else:
            print("invalid credentials")
            messages.error(request,"Invalid cradentials please fill correct details")
            return redirect("login")
    
    return render(request,"login.html")

def registerview(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        if len(password) < 8:
            messages.warning(request,"Password must be 8 characters!")
            return redirect("register")
        
        get_all_username=User.objects.filter(username=username)
        if get_all_username:
            messages.warning(request,"username already exist please use another username")
            return redirect("register")
        
        get_all_email = User.objects.filter(email=email)
        if get_all_email:
            messages.warning(request,"email already exist!")
            return redirect("register")
        
        new_user = User.objects.create_user(username=username,email=email,password=password)
        new_user.save()
        messages.success(request,"user created sucessfully :)")
        return redirect("login")
             
        
    return render(request,"register.html")

def logoutview(request):
    logout(request)
    return redirect("landing")
