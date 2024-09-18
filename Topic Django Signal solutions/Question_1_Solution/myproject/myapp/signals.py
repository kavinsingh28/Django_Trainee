# myapp/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from myapp.models import MyModel
import logging,time

# Configure logging
logging.basicConfig(filename='signals.log', level=logging.INFO)

@receiver(post_save, sender=MyModel)
def log_signal(sender, instance, **kwargs):
    # Log a message and the current timestamp
    logging.info(f"Signal received at {timezone.now()}")
    time.sleep(10)  # Creates delay of 10 sec
    logging.info(f"Signal processed at {timezone.now()}")
