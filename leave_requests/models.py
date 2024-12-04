from django.db import models
from django.contrib.auth.models import User

class LeaveRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_requests', null=True, blank=True)

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'), 
        ('rejected', 'Rejected'),
    ]

    start_date = models.DateField()
    end_date = models.DateField()
    raised_date = models.DateTimeField(auto_now_add=True)
    reason = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leave request from {self.start_date} to {self.end_date}"
