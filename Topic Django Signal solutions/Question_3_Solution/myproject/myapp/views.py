# myapp/views.py

# myapp/views.py

from django.db import transaction
from django.http import HttpResponse
from .signals import my_signal
from .models import MyModel

def create_instance_and_emit_signal(request):
    with transaction.atomic():
        print("Creating instance...")  # This should print to the console
        MyModel.objects.create(name="Original")
        my_signal.send(sender=None)
    
    # Check if instances exist in the database
    records = MyModel.objects.all()
    response = "Database records after transaction:<br>"
    for instance in records:
        response += f"{instance.name}<br>"
    return HttpResponse(response)
