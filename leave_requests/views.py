from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import LeaveRequest  # Make sure you have this model created
from .forms import LeaveRequestForm  # Make sure to create this form

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('leave_requests:home')  # Replace 'home' with your desired redirect URL
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'leave_requests/login.html')

def logout_view(request):
    logout(request)
    return redirect('leave_requests:login')  # Redirect to login page after logout

@login_required
def home(request):
    leave_requests = LeaveRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'leave_requests/home.html', {'leave_requests': leave_requests})

@login_required
def create_leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.user = request.user
            leave_request.save()
            return redirect('leave_requests:home')
    else:
        form = LeaveRequestForm()
    
    return render(request, 'leave_requests/create_leave_request.html', {'form': form})
