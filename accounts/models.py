from django.db import models
from django.contrib.auth.models import AbstractUser

class WorkerUser(AbstractUser):
    phone_number = models.CharField(max_length=13)
    job_title = models.CharField(max_length=140)
    rest_time = models.CharField(max_length=140)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
