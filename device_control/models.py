from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class DeviceControlItem(models.Model):
    text = models.CharField(max_length=100)
    due_date = models.DateField(default=timezone.now)
