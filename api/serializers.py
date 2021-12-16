from rest_framework import serializers
from .models import  (Devotion, PrayerList, Events, Announcements, Comments, PrayFor,Testimonies, ImageBoxes,VidBoxes)

class DevotionSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Devotion
        fields = ['id','user','username','title','message','slug','devotion_vid','date_posted']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

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

class CommentsSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Comments
        fields = ['id','user','username','devotion','comment','get_absolute_comment_url','date_commented']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

class PrayforSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = PrayFor
        fields = ['id','user','username','prayer','prayer_text','get_absolute_prayfor_url','date_posted']
        read_only_fields = ['user']

    def get_username(self, user):
        username = user.user.username
        return username

class TestimonySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model =Testimonies
        fields = ['id','user','username','testimony','date_posted']
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
        model = ImageBoxes
        fields = ['id','vid_url','date_posted']