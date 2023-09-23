from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

from tickets.models import Ticket
from .models import User


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Ticket.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def updateProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == True:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


post_save.connect(createProfile, sender=User)
post_save.connect(updateProfile, sender=Ticket)