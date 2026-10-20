from django.shortcuts import render,redirect
from accounts.models import Login
from django.contrib import messages


# Create your views here.
def login_view(request):
# return render(request,'accounts/login.html')
    if request.method == "POST":
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')

        try:
            # user = Login.objects.get(username = user_name, password =user_pass)
          if user_name == 'admin' and user_pass == '12345': 
            messages.success(request,"Login Successfuly !")
            return redirect('home')
        except Login.DoesNotExist:
            messages.error(request,"Invalid Username and password")
            return render (request,'accounts/login.html')
    return render(request,'accounts/login.html')


def home_view(request):
    return render(request,"home.html"   )