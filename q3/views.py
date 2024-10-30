from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import transaction
from .models import LogEntry

def test_signal_transaction(request):
    try:
        with transaction.atomic():
            user = User.objects.create(username="testuser")
            print("User created in view.")
            raise Exception("Simulating an error to trigger rollback")
    except Exception as e:
        print(e)

    # Checking if the User and LogEntry exist after the rollback

    user_exists = User.objects.filter(username="testuser").exists()
    log_entry_exists = LogEntry.objects.filter(message="User created").exists()
    print(f"User exists after rollback: {user_exists}")
    print(f"LogEntry exists after rollback: {log_entry_exists}")

    return render(request, "some_template.html")