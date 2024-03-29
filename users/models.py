from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image
from api.process_mail import send_my_mail
from django.conf import settings

DeUser = settings.AUTH_USER_MODEL


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(max_length=15, unique=True, help_text="please format should be +233")
    full_name = models.CharField(max_length=150, default="Fnet User")

    REQUIRED_FIELDS = ['username', 'phone', 'full_name']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="profile_user")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png", max_length=500, blank=True)

    def __str__(self):
        return self.user.username

    def get_username(self):
        return self.user.username

    def get_email(self):
        return self.user.email

    def get_full_name(self):
        return self.user.full_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def user_profile_pic(self):
        if self.profile_pic:
            return "http://127.0.0.1:8000" + self.profile_pic.url

        return ''
