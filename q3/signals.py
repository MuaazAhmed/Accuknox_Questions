from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import LogEntry

@receiver(post_save, sender=User)
def create_log_entry(sender, instance, **kwargs):
    LogEntry.objects.create(message="User created")  # Action in the signal
    print("LogEntry created by signal.")