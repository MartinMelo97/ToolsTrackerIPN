from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import WorkerUser

class WorkerUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        ('Worker Information', {
            'fields': ('job_title', 'rest_time')
        })
    )

admin.site.register(WorkerUser, WorkerUserAdmin)
