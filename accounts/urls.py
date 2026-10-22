from django.urls import path
from . import views

urlpatterns = [ 
     path('login/', views.login_view, name = 'login'),
     path('home/',views.home_view,name='home'),
     path('registration/',views.registration_view, name='registration'),
     path('admin_dashboard/',views.admin_dashboard__view, name = 'admin_dashboard')

]               


# accounts/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [ 
#     path('login/', views.login_view, name='login'),
#     path('home/', views.home_view, name='home'),
#     path('registration/', views.registration_view, name='registration'), # 👈 આ નામ HTML ના {% url 'registration' 
# ]
