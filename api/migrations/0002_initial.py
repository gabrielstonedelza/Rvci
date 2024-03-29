# Generated by Django 3.2.9 on 2022-10-11 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonies',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stories',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stories',
            name='viewers',
            field=models.ManyToManyField(blank=True, related_name='story_viewers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='prayerrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='notifications',
            name='notification_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_receiving_notification', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likestory',
            name='story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.stories'),
        ),
        migrations.AddField(
            model_name='likestory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='devotioncomment',
            name='devotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.dailydevotion'),
        ),
        migrations.AddField(
            model_name='devotioncomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_commenting', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dailydevotion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
