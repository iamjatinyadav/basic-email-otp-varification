from django.core.mail import send_mail
import random
from django.conf import settings
from django.contrib.auth import get_user_model


User = get_user_model()


def send_otp_via_mail(email):
    subject = "Your account verification mail"
    otp = random.randint(1000, 9999)
    message = f"Your otp is {otp}"
    email_from = settings.EMAIL_HOST
    send_mail(subject, message, email_from, [email])

    user_obj = User.objects.get(email=email)
    user_obj.otp = otp
    user_obj.save()
