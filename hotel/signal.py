from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.contrib.auth.models import User, Group
from django.contrib.auth.models import Group
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from hotel.models import Booking
from user.models import User

@receiver(post_save, sender=Booking)
def send_booking_email(sender, instance, created, **kwargs):
    if created:
        mail = instance.user.email
        subject = 'Booking Confirmation'
        message = f'Hi  {instance.user.first_name} {instance.user.last_name},\n\n Your Booking is confromed \n\nThank You!'
        recipient_list = [mail]
        try:
            send_mail(subject, message,
                      settings.EMAIL_HOST_USER, recipient_list)
        except Exception as e:
            print(f"Failed to send email to {instance.email}: {str(e)}")

        