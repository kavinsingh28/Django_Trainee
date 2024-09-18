# myapp/signals.py

from django.dispatch import Signal, receiver
from .models import MyModel

# Define a signal
my_signal = Signal()

# A simple signal receiver that modifies the database
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler running...")
    MyModel.objects.create(name="Signal Triggered")
