from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def user_saved_signal(sender, instance, **kwargs):
    print("Signal received. Processing...")
    time.sleep(5)  # Simulate a delay
    print("Signal processing completed.")