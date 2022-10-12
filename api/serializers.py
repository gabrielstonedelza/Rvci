from rest_framework import serializers
from .models import (DailyDevotion, PrayerRequest, Events, Announcements, ImageBoxes, VidBoxes, LiveNow, Stories,
                     Testimonies)
from users.models import Profile


class DevotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyDevotion
        fields = ['id', 'user', 'title', 'message', 'slug', 'date_posted', 'get_username', 'devotional_video',
                  'get_user_profile_pic', 'get_devotional_vid',]
        read_only_fields = ['user']


class StoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = ['id', 'user', 'story', 'date_posted', 'get_story_vid', 'get_user_pic', 'get_username']
        read_only_fields = ['user']


class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerRequest
        fields = ['id', 'user', 'prayer_title', 'prayer_request', 'views', 'slug', 'date_posted']
        read_only_fields = ['user']


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'title', 'event_date', 'event_time', 'event_poster', 'event_description', 'views', 'slug',
                'get_event_poster', 'date_posted']


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = ['id', 'title', 'message', 'date_posted', 'slug']


class ImageBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBoxes
        fields = ['id', 'caption', 'image', 'date_posted']


class VidBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = VidBoxes
        fields = ['id', 'vid_url', 'date_posted']


class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveNow
        fields = ['id', 'live_url', 'date_posted']


class TestimoniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonies
        fields = ['id', 'user', 'testimony', 'date_posted', 'get_username', 'get_user_pic', 'views']

        read_only_fields = ['user']
