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

    REQUIRED_FIELDS = ['email', 'phone', 'full_name']
    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     if self.email:
    #         send_my_mail(f"Hi from RVCI", settings.EMAIL_HOST_USER, self.email, {"name": self.username},
    #                      "email_templates/registration_success.html")



class Profile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="profile_user")
    profile_pic = models.ImageField(upload_to="profile_pics", default="default_user.png",max_length=500,blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def user_profile_pic(self):
        if self.profile_pic:
            return "https://rvci.xyz" + self.profile_pic.url

        return ''