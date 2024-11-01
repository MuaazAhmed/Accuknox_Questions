from django.shortcuts import render
from django.contrib.auth.models import User
import time

def test_signal(request):
    start_time = time.time()
    user = User.objects.create(username="testuser")
    end_time = time.time()

    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")
    return render(request, "some_template.html")