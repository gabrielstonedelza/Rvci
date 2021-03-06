from django.shortcuts import get_object_or_404
from .models import  (Devotion, PrayerList, Events, Announcements, PrayFor, ImageBoxes,VidBoxes,LiveNow,Stories,DailyVids)
from .serializers import (DevotionSerializer,PrayerListSerializer,EventsSerializer,PrayforSerializer,AnnouncementSerializer,ImageBoxSerializer,VidBoxSerializer,LiveSerializer,StoriesSerializer,DailyVidsSerializer)
from datetime import datetime,date,time,timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response

from users.serializers import ProfileSerializer
from users.models import User,Profile
from django.utils import timezone

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_stories(request):
    serializer = StoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_stories(request):
    # time_threshold = datetime.now(timezone.utc) - timedelta(hours=10)
    # query = Stories.objects.filter(time_posted__gt=time_threshold)
    my_time = datetime.now()

    query = Stories.objects.all().order_by('-date_posted')
    serializer = StoriesSerializer(query,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_stories(request,pk):
    user = get_object_or_404(User,pk=pk)
    query = Stories.objects.filter(user=user).order_by('-date_posted')
    serializer = StoriesSerializer(query,many=True)
    return Response(serializer.data)


# add devotion
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_devotion(request):
    serializer = DevotionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get all devotions from users
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_devotions(request):
    devotions = Devotion.objects.all().order_by('-date_posted')
    serializer = DevotionSerializer(devotions,many=True)
    return Response(serializer.data)

# get request.user's devotions
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_devotions(request):
    devotions = Devotion.objects.filter(user=request.user).order_by('-date_posted')
    serializer = DevotionSerializer(devotions, many=True)
    return Response(serializer.data)

# devotion detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def devotion_detail(request,slug):
    dev_detail = get_object_or_404(Devotion,slug=slug)
    if dev_detail:
        dev_detail.views +=1
        dev_detail.save()
        if not Devotion.objects.filter(id=request.user.id).exists():
            dev_detail.likes.add(request.user)
        else:
            dev_detail.likes.remove(request.user)

    serializer = DevotionSerializer(dev_detail,many=False)
    return Response(serializer.data)

# post prayer request
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_prayer(request):
    serializer = PrayerListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get all prayers
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_prayer_lists(request):
    prayer_lists = PrayerList.objects.all().order_by('-date_posted')
    serializer = PrayerListSerializer(prayer_lists,many=True)
    return Response(serializer.data)

# get request.user's prayerlists
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_prayer_lists(request):
    prayer_lists = PrayerList.objects.filter(user=request.user).order_by('-date_posted')
    serializer = PrayerListSerializer(prayer_lists,many=True)
    return Response(serializer.data)

# prayerlist detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def prayer_detail(request,slug):
    prayer = get_object_or_404(PrayerList,slug=slug)
    if prayer:
        prayer.views +=1
        prayer.save()
    serializer = PrayerListSerializer(prayer,many=False)
    return Response(serializer.data)

# add new event
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_event(request):
    serializer = EventsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get the latest event
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_current_event(request):
    event = Events.objects.all().order_by('-date_posted')[:1]
    serializer = EventsSerializer(event,many=True)
    return Response(serializer.data)

# event detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def event_detail(request,slug):
    event = get_object_or_404(Events,slug=slug)
    if event:
        event.views +=1
        event.save()
    serializer = EventsSerializer(event,many=False)
    return Response(serializer.data)

# add announcements
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_announcements(request):
    serializer = AnnouncementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get the latest announcement
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_current_announcement(request):
    event = Announcements.objects.all().order_by('-date_posted')[:1]
    serializer = AnnouncementSerializer(event,many=True)
    return Response(serializer.data)

# announcement detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def announcement_detail(request,id):
    announcement = get_object_or_404(Announcements,id=id)
    serializer = AnnouncementSerializer(announcement,many=False)
    return Response(serializer.data)

# pray for user
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def pray_for_user(request,id):
    prayer = get_object_or_404(PrayerList,id=id)
    serializer = PrayforSerializer(prayer,data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get pray for lists
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_pray_for_lists(request,id):
    prayer = get_object_or_404(PrayerList, id=id)
    serializer = PrayforSerializer(prayer,many=True)
    return Response(serializer.data)

# pray for detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def prayfor_detail(request,id):
    prayer = get_object_or_404(PrayerList, id=id)
    serializer = PrayforSerializer(prayer,many=False)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_users(request):
    users = Profile.objects.exclude(id=request.user.id)
    serializer = ProfileSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_images(request):
    serializer = ImageBoxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_images(request):
    images = ImageBoxes.objects.all().order_by('-date_posted')
    serializer = ImageBoxSerializer(images,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_vids(request):
    serializer = VidBoxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_videos(request):
    all_vids = VidBoxes.objects.all().order_by('-date_posted')
    serializer = VidBoxSerializer(all_vids,many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_live(request):
    serializer = LiveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_live_now(request):
    live_now = LiveNow.objects.all().order_by('-date_posted')
    serializer = LiveSerializer(live_now,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_daily_vid(request):
    live_now = DailyVids.objects.all().order_by('-date_posted')
    serializer = DailyVidsSerializer(live_now,many=True)
    return Response(serializer.data)