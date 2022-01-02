from django.db import models
from django.conf import settings
from django.utils import timezone
from PIL import Image
from django.utils.text import slugify
from .validator import validate_story_size
from .validator import validate_devotion_size
from datetime import datetime,date,time,timedelta

User = settings.AUTH_USER_MODEL

GALLERY_TYPE = (
    ("Image","Image"),
    ("Video","video"),
)

class Devotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=200)
    message = models.TextField()
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_devotion_url(self):
        return f"/{self.slug}/"

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)


class Stories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.FileField(upload_to="stories",validators=[validate_story_size])
    time_posted = models.TimeField(default=datetime.now)
    date_posted = models.DateField(default=datetime.now)

    def __str__(self):
        return f"{self.user.username} added a new story"

    def get_story_vid(self):
        if self.story:
            return "https:www.rvci.xyz" + self.story.url
        return ""
    def get_story_user(self):
        return "https:www.rvci.xyz" + self.user.profile.profile_pic.url

class PrayerList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prayer_title = models.CharField(max_length=200)
    prayer_request = models.TextField()
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_absolute_prayerlist_url(self):
        return f"/{self.slug}/"

    def save(self, *args, **kwargs):
        value = self.prayer_title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    # def get_user_profile_pic(self):
    #
    #     return "https://rvci.xyz" + self.user.profile.profile_pic.url

class Events(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateTimeField(default=timezone.now)
    event_time = models.DateTimeField(default=timezone.now)
    event_description = models.TextField()
    event_poster = models.ImageField(upload_to="event_posters")
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_event_url(self):
        return f"/{self.slug}/"

    def get_event_poster(self):
        if self.event_poster:
            return "https://rvci.xyz" + self.event_poster.url

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

    def get_absolute_announcement_url(self):
        return f"/{self.slug}/"


    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class PrayFor(models.Model):
    prayer = models.ForeignKey(PrayerList, on_delete=models.CASCADE)
    user = models.ManyToManyField(User,related_name="prayee")
    prayer_text = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_absolute_prayfor_url(self):
        return f"/{self.id}/"

class ImageBoxes(models.Model):
    caption = models.CharField(max_length=100)
    image = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption

class VidBoxes(models.Model):
    vid_url = models.CharField(max_length=100,default="")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vid_url

class LiveNow(models.Model):
    live_url = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.live_url
