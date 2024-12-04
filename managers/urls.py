from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('handle-request/<int:request_id>/', views.handle_request, name='handle_request'),
]
