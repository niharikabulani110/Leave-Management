from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Manager
from leave_requests.models import LeaveRequest

@login_required
def manager_dashboard(request):
    try:
        manager = Manager.objects.get(user=request.user)
        managed_users = manager.managed_users.all()
        leave_requests = LeaveRequest.objects.filter(user__in=managed_users).order_by('-created_at')
        return render(request, 'managers/dashboard.html', {
            'leave_requests': leave_requests,
            'managed_users': managed_users
        })
    except Manager.DoesNotExist:
        messages.error(request, "You don't have manager privileges.")
        return redirect('home')

@login_required
def handle_request(request, request_id):
    try:
        manager = Manager.objects.get(user=request.user)
        leave_request = get_object_or_404(LeaveRequest, id=request_id)
        
        # Verify the leave request belongs to a managed user
        if leave_request.user not in manager.managed_users.all():
            messages.error(request, "You don't have permission to handle this request.")
            return redirect('manager_dashboard')
        
        action = request.POST.get('action')
        if action == 'approve':
            leave_request.status = 'accepted'
            messages.success(request, 'Leave request approved successfully.')
        elif action == 'reject':
            leave_request.status = 'rejected'
            messages.success(request, 'Leave request rejected successfully.')
        
        leave_request.save()
        return redirect('manager_dashboard')
        
    except Manager.DoesNotExist:
        messages.error(request, "You don't have manager privileges.")
        return redirect('home')
