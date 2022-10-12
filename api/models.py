from django.db import models
from django.conf import settings
from django.utils import timezone
from PIL import Image
from django.utils.text import slugify
from .validator import validate_story_size, validate_devotion_size, validate_post_duration
from datetime import datetime, date, time, timedelta
from users.models import Profile

User = settings.AUTH_USER_MODEL
# Create your models here.
READ_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

NOTIFICATIONS_STATUS = (
    ("Read", "Read"),
    ("Not Read", "Not Read"),
)

NOTIFICATIONS_TRIGGERS = (
    ("Triggered", "Triggered"),
    ("Not Triggered", "Not Triggered"),
)

GALLERY_TYPE = (
    ("Image", "Image"),
    ("Video", "video"),
)

PHOTO_CATEGORY = (
    ("Regular", "Regular"),
    ("Miss Refined", "Miss Refined"),
    ("Traditional", "Traditional"),
)


class DailyDevotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    message = models.TextField(blank=True)
    devotional_video = models.FileField(upload_to="devotion_videos", null=True, validators=[validate_devotion_size])
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_username(self):
        return self.user.username

    def get_user_profile_pic(self):
        user = Profile.objects.get(user=self.user)
        if user:
            return "http://127.0.0.1:8000" + user.profile_pic.url
        return ""

    def get_devotional_vid(self):
        if self.devotional_video:
            return "http://127.0.0.1:8000" + self.devotional_video.url
        return ""


# comment on devotion
class DevotionComment(models.Model):
    devotion = models.ForeignKey(DailyDevotion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_commenting")
    comment = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Stories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.FileField(upload_to="stories", validators=[validate_devotion_size])
    views = models.IntegerField(default=0)
    viewers = models.ManyToManyField(User, blank=True, related_name="story_viewers")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} added a new story"

    def get_username(self):
        return self.user.username

    def get_story_vid(self):
        if self.story:
            return "http://127.0.0.1:8000" + self.story.url
        return ""

    def get_user_pic(self):
        my_user = Profile.objects.get(user=self.user)
        if my_user:
            return "http://127.0.0.1:8000" + my_user.profile_pic.url
        return ""


class PrayerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prayer_title = models.CharField(max_length=200)
    prayer_request = models.TextField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prayer request from {self.user.username}"

    def save(self, *args, **kwargs):
        value = self.prayer_title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_username(self):
        return self.user.username

    def get_user_pic(self):
        my_user = Profile.objects.get(user=self.user)
        if my_user:
            return "http://127.0.0.1:8000" + my_user.profile_pic.url
        return ""


class Events(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.CharField(max_length=200)
    event_time = models.CharField(max_length=200)
    event_description = models.TextField()
    event_poster = models.ImageField(upload_to="event_posters", blank=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_event_poster(self):
        if self.event_poster:
            return "http://127.0.0.1:8000" + self.event_poster.url

        return ''

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
        img = Image.open(self.event_poster.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.event_poster.path)


class Announcements(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class ImageBoxes(models.Model):
    caption = models.CharField(max_length=100)
    image = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption


class VidBoxes(models.Model):
    vid_url = models.CharField(max_length=100, default="")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vid_url


class LiveNow(models.Model):
    live_url = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.live_url


class Testimonies(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testimony = models.TextField()
    views = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimony from {self.user.username}"

    def get_username(self):
        return self.user.username

    def get_user_pic(self):
        my_user = Profile.objects.get(user=self.user)
        if my_user:
            return "http://127.0.0.1:8000" + my_user.profile_pic.url
        return ""


class Notifications(models.Model):
    notification_id = models.CharField(max_length=100, blank=True, default="")
    notification_title = models.CharField(max_length=255, blank=True)
    notification_message = models.TextField(blank=True)
    read = models.CharField(max_length=20, choices=NOTIFICATIONS_STATUS, default="Not Read")
    notification_trigger = models.CharField(max_length=255, choices=NOTIFICATIONS_TRIGGERS, default="Triggered",
                                            blank=True)
    notification_from = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    notification_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_receiving_notification",
                                        null=True)
    devotion_slug = models.CharField(max_length=255, blank=True)
    story_id = models.CharField(max_length=255, blank=True)
    prayer_slug = models.CharField(max_length=255, blank=True)
    event_slug = models.CharField(max_length=255, blank=True)
    announcement_slug = models.CharField(max_length=255, blank=True)
    image_id = models.CharField(max_length=255, blank=True)
    video_id = models.CharField(max_length=255, blank=True, default='')
    live_now_id = models.CharField(max_length=255, blank=True, default='')
    testimony_id = models.CharField(max_length=255, blank=True, default='')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notification_title

    def get_notification_from_pic(self):
        user = User.objects.get(username=self.notification_from.username)
        my_user = Profile.objects.get(user=user)
        if my_user:
            return "http://127.0.0.1:8000" + my_user.profile_pic.url
        return ""


class LikeStory(models.Model):
    story = models.ForeignKey(Stories, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    date_posted = models.DateTimeField(auto_now_add=True, )

    def get_user_pic(self):
        my_user = Profile.objects.get(user=self.user)
        if my_user:
            return "http://127.0.0.1:8000" + my_user.profile_pic.url
        return ""
