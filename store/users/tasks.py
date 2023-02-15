from celery import shared_task
from users.models import User, EmailVerification

from django.utils.timezone import now
from datetime import timedelta
import uuid


@shared_task
def send_email_verification(user_id):
    user=User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=24)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verification_email()
