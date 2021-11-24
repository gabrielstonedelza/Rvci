from django.shortcuts import get_object_or_404
from .models import  Devotion,PrayerList,Stories,Events,Announcements,Likes,Comments,PrayFor,NotifyMe
from .serializers import DevotionSerializer,PrayerListSerializer,StoriesSerializer,EventsSerializer,LikesSerializer,CommentsSerializer,PrayforSerializer,NotifymeSerializer,AnnouncementSerializer

# Create your views here.
