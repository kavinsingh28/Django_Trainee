# import threading
# from django.dispatch import Signal, receiver

# my_signal = Signal()

# @receiver(my_signal)
# def my_signal_handler(sender, **kwargs):
#     print(f"Signal received in thread: {threading.current_thread().name}")

# def emit_signal():
#     print(f"Emitting signal from thread: {threading.current_thread().name}")
#     my_signal.send(sender=None)

# if __name__ == "__main__":
#     emit_signal()
    
#     new_thread = threading.Thread(target=emit_signal)
#     new_thread.start()
#     new_thread.join()


from django.db import models, transaction
from django.dispatch import Signal, receiver
from django.db import connection

# Define a simple model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Define a signal
my_signal = Signal()

# A simple signal receiver that modifies the database
@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print("Signal handler running...")
    MyModel.objects.create(name="Signal Triggered")

# Function to create a model instance and emit the signal
def create_instance_and_emit_signal():
    with transaction.atomic():
        print("Creating instance...")
        MyModel.objects.create(name="Original")
        my_signal.send(sender=None)  # Emit signal within transaction
        # Uncomment the line below to simulate an error
        # raise Exception("Simulating an error to check transaction rollback")

# Main execution
if __name__ == "__main__":
    # Setup: Create a new database table for MyModel
    MyModel.objects.all().delete()  # Clear table for test

    create_instance_and_emit_signal()

    # Check if instances exist in the database
    print("Database records after transaction:")
    for instance in MyModel.objects.all():
        print(instance.name)
