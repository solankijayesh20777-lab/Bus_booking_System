from django.shortcuts import render,redirect
from accounts.models import Login
from django.contrib import messages
from django.db import connection


# Create your views here.
def login_view(request):
# return render(request,'accounts/login.html')
    if request.method == "POST":
        user_name = request.POST.get('username')
        user_pass = request.POST.get('password')

        try:
            user = Login.objects.get(username = user_name, password =user_pass)
        #   if user_name == 'admin' and user_pass == '12345': 
            messages.success(request,"Login Successfuly !")
            return redirect('home')
        except Login.DoesNotExist:
            messages.error(request,"Invalid Username and password")
            return render (request,'accounts/login.html')
    return render(request,'accounts/login.html')


# write register_view find values login fields

def registration_view(request):
    if request.method == "POST":
        f_name = request.POST.get('fullname')
        u_name = request.POST.get('username')
        u_email = request.POST.get('email')
        u_phone = request.POST.get('phone')
        u_gender = request.POST.get('gender')
        u_pass = request.POST.get('password')

        with connection.cursor() as cursor:
           insert_query = """
            insert into registration (fullname,username,email,phone,gender,password) values (%s,%s,%s,%s,%s,%s);
            """
           cursor.execute(insert_query,[f_name,u_name,u_email,u_phone,u_gender,u_pass])
        messages.success(request,"Rigistraion Successful !")
        return redirect('login')

    return render(request,'accounts/registration.html')

def home_view(request):
    return render(request,"home.html"   )