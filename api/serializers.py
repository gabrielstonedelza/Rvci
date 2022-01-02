from rest_framework import serializers
from .models import  (Devotion, PrayerList, Events, Announcements, PrayFor,ImageBoxes,VidBoxes,LiveNow,Stories)

class DevotionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Devotion
        fields = ['id','user','username','title','message','slug','date_posted']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

class StoriesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    user_pic = serializers.SerializerMethodField('get_user_pic')

    class Meta:
        model = Stories
        fields = ['id', 'user', 'username', 'story', 'date_posted','time_posted','user_pic','get_story_vid']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

    def get_user_pic(self, profile):
        user_pic = profile.user.profile_pic.url
        return user_pic

class PrayerListSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = PrayerList
        fields = ['id','user','username','prayer_title','prayer_request','views','slug','get_absolute_prayerlist_url','date_posted']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id','title','event_date','event_time','event_poster','event_description', 'views','slug','get_absolute_event_url','get_event_poster','date_posted']

class AnnouncementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Announcements
        fields = ['id','title','message','get_absolute_announcement_url']

class PrayforSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = PrayFor
        fields = ['id','user','username','prayer','prayer_text','get_absolute_prayfor_url','date_posted']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

class ImageBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBoxes
        fields = ['id','caption','image','date_posted']

class VidBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = VidBoxes
        fields = ['id','vid_url','date_posted']

class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveNow
        fields = ['id','live_url','date_posted']