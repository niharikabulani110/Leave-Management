from django.urls import path
from . import views

app_name = 'leave_requests'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_leave_request, name='create_leave_request'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
] 