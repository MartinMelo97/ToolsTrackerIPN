from django.db import models
from accounts.models import WorkerUser

class WorkTool(models.Model):
    name = models.CharField(max_length=140)
    user_id = models.ForeignKey(WorkerUser, related_name='tools', on_delete=models.CASCADE, blank=True, null=True)
    serial_number = models.CharField(max_length=140)
    model = models.CharField(max_length=140)
    has_been_in_mainteance = models.BooleanField(default=False)
    mainteance_date = models.DateField(blank=True, null=True)
    is_in_maintain = models.BooleanField(default=False)
    specifications = models.TextField(blank=True, null=True)
    has_tracker = models.BooleanField(default=False)
    tracker_id = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name
