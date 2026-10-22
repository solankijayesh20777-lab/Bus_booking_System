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

        with connection.cursor() as cursor:
            select_query = """
                select id,username from registration where username = %s and password = %s;
                """
            cursor.execute(select_query,[user_name,user_pass])
            user_record = cursor.fetchone()

        if user_record is not None:
            request.session['user_id'] = user_record[0]
            request.session['username'] = user_record[1]
            messages.success(request,"Login Successfully !")
            return  redirect('home')


        else:
            context = {
                'error':"Invalid username and password Plise Try again !"
            }

        # try:
            # user = Login.objects.get(username = user_name, password =user_pass)
        #   if user_name == 'admin' and user_pass == '12345': 
          
        # except Login.DoesNotExist:
            # messages.error(request,"Invalid Username and password")
            return render (request,'accounts/login.html',context)
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

# home_view

def home_view(request):
    user_logged = request.session.get('username')

    context = {
        'username':user_logged
    }
    return render(request,"home.html"   )


#  admin add bus moduls

def admin_dashboard__view(request):
    if request.method == "POST" and 'add_bus' in request.POST:
        b_name = request.POST.get('bus_name')
        b_type = request.POST.get('bus_type')
        b_source = request.POST.get('source')
        b_dest = request.POST.get('destination')
        b_time = request.POST.get('departs_time')
        b_price = request.POST.get('price')
        b_seats = request.POST.get('total_seats')
        b_status = request.POST.get('status')

        # insert bus query
        
        with connection.cursor() as cursor:
            insert_query = """
                    insert into buses(bus_name,bus_type,source,destination, departs_time, price,total_seats,status) 
                    values (%s,%s,%s,%s,%s,%s,%s,%s)
                    """

            cursor.execute(insert_query, [b_name,b_type,b_source,b_dest,b_time,b_price,b_seats,b_status])
        messages.success(request,"New Bus Add Succefully !")
        return redirect('admin_dashboard')

        #  delete bus query
    elif request.method == "POST" and 'delete_bus' in request.POST:
        bus_id = request.POST.get('bus_id')
        
        with connection.cursor() as cursor:
            delete_query = "delete from buses where id = %s;"
            cursor.execute(delete_query,[bus_id])
            
        messages.success(request,"Deleted Bus")
        return redirect('admin_dashboard')
  
    # all bus show 
        
    with connection.cursor() as cursor:
            cursor.execute("select id,bus_name,bus_type,source,destination,departs_time,price,total_seats,status from buses;")
            buses_list = cursor.fetchall()
            
    context = {
        'buses':buses_list
    }
    return render(request,'accounts/admin_dashboard.html',context)
