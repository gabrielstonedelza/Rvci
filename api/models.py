from django.db import models
from django.conf import settings
from django.utils import timezone
from PIL import Image
from django.utils.text import slugify

User = settings.AUTH_USER_MODEL

class Devotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    devotion_vid = models.FileField(upload_to="dev-vids")
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_devotion_url(self):
        return f"/{self.slug}/"

    def get_devotion_vid(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.devotion_vid.url

        return ''

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

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

class Stories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.FileField(upload_to="stories")
    views = models.ManyToManyField(User,related_name="viewers")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_absolute_story_url(self):
        return f"/{self.slug}/"

    def get_story_vid(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.story.url
        return ''

class Events(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateTimeField(default=timezone.now)
    event_time = models.DateTimeField(default=timezone.now)
    event_poster = models.ImageField(upload_to="event_posters")
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=100, default='')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_event_url(self):
        return f"/{self.slug}/"

    def get_event_poster(self):
        if self.image:
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

    def get_absolute_announcement_url(self):
        return f"/{self.slug}/"


    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Likes(models.Model):
    devotion = models.ForeignKey(Devotion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="likee")
    likes = models.IntegerField(default=0)
    date_liked = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.devotion.title
    def get_absolute_like_url(self):
        return f"/{self.id}/"

class Comments(models.Model):
    devotion = models.ForeignKey(Devotion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="commentee")
    comment = models.TextField()
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.devotion.title

    def get_absolute_comment_url(self):
        return f"/{self.id}/"

class PrayFor(models.Model):
    prayer = models.ForeignKey(PrayerList, on_delete=models.CASCADE)
    user = models.ManyToManyField(User,related_name="prayee")
    prayer_text = models.TextField(blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username

    def get_absolute_prayfor_url(self):
        return f"/{self.id}/"

class NotifyMe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify_title = models.CharField(max_length=100, default="New Notification")
    notify_alert = models.CharField(max_length=100)
    notify_from = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="notification_from")
    read = models.BooleanField(default=False)
    devotion_slug = models.CharField(max_length=100)
    prayerlist_slug = models.CharField(max_length=100, blank=True)
    story_slug = models.CharField(max_length=100, blank=True)
    event_slug = models.CharField(max_length=100, blank=True)
    announcement_slug = models.CharField(max_length=100, blank=True)
    likes_slug = models.CharField(max_length=100, blank=True)
    comments_slug = models.CharField(max_length=100, blank=True)
    prayfor_slug = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, default='')
    date_notified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"New {self.notify_title} notification sent to  {self.user}"


    def get_absolute_notification_url(self):
        return f"/{self.slug}/"

    def save(self, *args, **kwargs):
        value = self.notify_title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)