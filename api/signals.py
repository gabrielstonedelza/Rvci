from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Devotion,PrayerList,Stories,Events,Announcements,Comments,PrayFor,NotifyMe
from django.shortcuts import get_object_or_404
from django.conf import settings
from users.models import User

DeUser = settings.AUTH_USER_MODEL

@receiver(post_save,sender=Devotion)
def create_devotion(sender,created,instance, **kwargs):
    title = "New Devotion"
    message = f"Enjoy today's devotion from {instance.user}"
    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            NotifyMe.objects.create(user=i, notify_title=title, notify_alert=message, notify_from=instance.user,devotion_slug=instance.slug)


@receiver(post_save,sender=PrayerList)
def create_prayerlist(sender,created,instance, **kwargs):
    title = "New Prayer"
    message = f"{instance.user} added a new prayer request"
    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            NotifyMe.objects.create(user=i, notify_title=title, notify_alert=message, notify_from=instance.user,prayerlist_slug=instance.slug)


@receiver(post_save, sender=Stories)
def create_stories(sender, created, instance, **kwargs):
    title = f"Story from {instance.user}"
    message = f"{instance.user} added posted a new story"
    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            NotifyMe.objects.create(user=i, notify_title=title, notify_alert=message, notify_from=instance.user,story_slug=instance.pk)

@receiver(post_save, sender=Events)
def create_event(sender, created, instance, **kwargs):
    title = f"New event from RVCI"
    message = f"RVCI added a new event"
    users = User.objects.exclude(id=1)
    admin_user = User.objects.get(id=1)

    if created:
        for i in users:
            NotifyMe.objects.create(user=i, notify_title=title, notify_alert=message, notify_from=admin_user,event_slug=instance.slug)


@receiver(post_save, sender=Announcements)
def create_announcement(sender, created, instance, **kwargs):
    title = f"New announcement from RVCI"
    message = f"Read RVCI announcement today"
    users = User.objects.exclude(id=1)
    admin_user = User.objects.get(id=1)

    if created:
        for i in users:
            NotifyMe.objects.create(user=i, notify_title=title, notify_alert=message, notify_from=admin_user,announcement_slug=instance.slug)

@receiver(post_save, sender=Comments)
def create_comment(sender, created, instance, **kwargs):
    title = f"New devotion comment"
    message = f"{instance.user} just commented your devotion {instance.devotion.title}"

    if created:
        NotifyMe.objects.create(user=instance.devotion.user, notify_title=title, notify_alert=message, notify_from=instance.user,comments_slug=instance.pk)

@receiver(post_save, sender=PrayFor)
def create_prayfor(sender, created, instance, **kwargs):
    title = f"{instance.user} just prayed for you"
    message = f"{instance.user} just prayed on your prayer {instance.prayer.prayer_title}"
    users = User.objects.exclude(id=instance.user.id)

    if created:
        for i in users:
            NotifyMe.objects.create(user=i, notify_title=title, notify_alert=message, notify_from=instance.user,prayfor_slug=instance.slug)