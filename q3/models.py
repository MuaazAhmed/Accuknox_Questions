from django.db import models
from django.contrib.auth.models import User

class LogEntry(models.Model):
    message = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)