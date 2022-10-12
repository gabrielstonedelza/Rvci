from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (DailyDevotion, PrayerRequest, Events, Announcements, Testimonies, LiveNow,
                     Stories, Notifications)
from django.shortcuts import get_object_or_404
from django.conf import settings
from users.models import User

DeUser = settings.AUTH_USER_MODEL


@receiver(post_save, sender=LiveNow)
def create_announcement(sender, created, instance, **kwargs):
    title = f"Live Now"
    message = f"RVCI is live now"
    users = User.objects.exclude(id=1)
    admin_user = User.objects.get(id=1)

    if created:
        for i in users:
            Notifications.objects.create(notification_to=i, notification_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=admin_user,
                                         live_now_id=instance.id)


@receiver(post_save, sender=Stories)
def create_story(sender, created, instance, **kwargs):
    title = "New Story"
    message = f"{instance.user.username} added to their story"
    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(notification_to=i, notification_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=instance.user,
                                         story_id=instance.id)


@receiver(post_save, sender=Testimonies)
def create_testimony(sender, created, instance, **kwargs):
    title = "New Testimony"
    message = f"{instance.user.username} added a new testimony"
    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(notification_to=i, notification_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=instance.user,
                                         testimony_id=instance.id)


@receiver(post_save, sender=DailyDevotion)
def create_devotion(sender, created, instance, **kwargs):
    title = "New Daily Devotion"
    message = f"Enjoy today's devotion from {instance.user.username}"
    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(notification_to=i, notification_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=instance.user,
                                         devotion_slug=instance.slug)


@receiver(post_save, sender=PrayerRequest)
def create_prayerList(sender, created, instance, **kwargs):
    title = "New Prayer"
    message = f"{instance.user.username} added a new prayer request"
    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            Notifications.objects.create(notification_to=i, notification_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=instance.user,
                                         prayer_slug=instance.slug)


@receiver(post_save, sender=Events)
def create_event(sender, created, instance, **kwargs):
    title = f"New event from RVCI"
    message = f"RVCI added a new event"
    users = User.objects.exclude(id=1)
    admin_user = User.objects.get(id=1)

    if created:
        for i in users:
            Notifications.objects.create(notification_to=i, notification_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=admin_user,
                                         prayer_slug=instance.slug)


@receiver(post_save, sender=Announcements)
def create_announcement(sender, created, instance, **kwargs):
    title = f"New announcement from RVCI"
    message = f"Read RVCI announcement today"
    users = User.objects.exclude(id=1)
    admin_user = User.objects.get(id=1)

    if created:
        for i in users:
            Notifications.objects.create(notification_to=i, notification_id=instance.id, notification_title=title,
                                         notification_message=message, notification_from=admin_user,
                                         announcement_slug=instance.slug)
