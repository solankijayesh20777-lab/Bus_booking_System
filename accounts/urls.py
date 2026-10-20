from django.urls import path
from .views import login_views

urlpatterns = [ 
    path('login/', views.login_view, name = 'login'),
    path('home/',views.home_views,name='home'),

]               