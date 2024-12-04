from django.contrib import admin
from .models import Manager

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_managed_users')
    filter_horizontal = ('managed_users',)

    def get_managed_users(self, obj):
        return ", ".join([user.username for user in obj.managed_users.all()])
    get_managed_users.short_description = 'Managed Users'
