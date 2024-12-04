from django.contrib import admin
from .models import LeaveRequest

@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'status', 'reason')
    list_filter = ('status',)
    search_fields = ('reason',)
