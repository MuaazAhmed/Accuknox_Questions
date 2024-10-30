from django.shortcuts import render
from django.contrib.auth.models import User
import threading

def test_signal(request):
    print(f"Caller thread ID: {threading.get_ident()}")
    user = User.objects.create(username="testuser")
    return render(request, "some_template.html")