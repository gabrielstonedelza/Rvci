from django.shortcuts import get_object_or_404
from .models import (DailyDevotion, PrayerRequest, Events, Announcements, Testimonies, ImageBoxes, VidBoxes, LiveNow,
                     Notifications,
                     Stories)
from .serializers import (DevotionSerializer, PrayerRequestSerializer, EventsSerializer, AnnouncementSerializer,
                          ImageBoxSerializer, VidBoxSerializer, LiveSerializer, StoriesSerializer)
from datetime import datetime, date, time, timedelta
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response

from users.serializers import ProfileSerializer
from users.models import User, Profile
from django.utils import timezone
from .validator import validate_story_size, validate_devotion_size


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_stories(request):
    serializer = StoriesSerializer(data=request.data)
    if serializer.is_valid():
        story_file = serializer.validated_data.get('story')
        validate_devotion_size(story_file)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# add devotion
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_devotion(request):
    serializer = DevotionSerializer(data=request.data)
    if serializer.is_valid():
        devotional_file = serializer.validated_data.get('devotional_video')
        validate_devotion_size(devotional_file)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_stories(request):
    # time_threshold = datetime.now(timezone.utc) - timedelta(hours=10)
    # query = Stories.objects.filter(time_posted__gt=time_threshold)
    my_time = datetime.now()
    time_24_hours_ago = datetime.now() - timedelta(days=1)
    all_stories = Stories.objects.all().order_by("-date_posted")

    stories = Stories.objects.filter(date_posted__gte=time_24_hours_ago)
    serializer = StoriesSerializer(stories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_stories(request, pk):
    user = get_object_or_404(User, pk=pk)
    query = Stories.objects.filter(user=user).order_by('-date_posted')
    serializer = StoriesSerializer(query, many=True)
    return Response(serializer.data)


# get all devotions from users
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_devotions(request):
    devotions = DailyDevotion.objects.all().order_by('-date_posted')
    serializer = DevotionSerializer(devotions, many=True)
    return Response(serializer.data)


# get request.user's devotions
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_devotions(request):
    devotions = DailyDevotion.objects.filter(user=request.user).order_by('-date_posted')
    serializer = DevotionSerializer(devotions, many=True)
    return Response(serializer.data)


# devotion detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def devotion_detail(request, slug):
    dev_detail = get_object_or_404(DailyDevotion, slug=slug)
    serializer = DevotionSerializer(dev_detail, many=False)
    return Response(serializer.data)


# post prayer request
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def post_prayer(request):
    serializer = PrayerRequestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get all prayers
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_prayer_request_lists(request):
    prayer_lists = PrayerRequest.objects.all().order_by('-date_posted')
    serializer = PrayerRequestSerializer(prayer_lists, many=True)
    return Response(serializer.data)


# get request.user's prayerlists
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_prayer_lists(request):
    prayer_lists = PrayerRequest.objects.filter(user=request.user).order_by('-date_posted')
    serializer = PrayerRequestSerializer(prayer_lists, many=True)
    return Response(serializer.data)


# prayerlist detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def prayer_detail(request, slug):
    prayer = get_object_or_404(PrayerRequest, slug=slug)
    if prayer:
        prayer.views += 1
        prayer.save()
    serializer = PrayerRequestSerializer(prayer, many=False)
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
    serializer = EventsSerializer(event, many=True)
    return Response(serializer.data)


# event detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def event_detail(request, slug):
    event = get_object_or_404(Events, slug=slug)
    if event:
        event.views += 1
        event.save()
    serializer = EventsSerializer(event, many=False)
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
    serializer = AnnouncementSerializer(event, many=True)
    return Response(serializer.data)


# announcement detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def announcement_detail(request, slug):
    announcement = get_object_or_404(Announcements, slug=slug)
    serializer = AnnouncementSerializer(announcement, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_users(request):
    users = Profile.objects.exclude(id=request.user.id)
    serializer = ProfileSerializer(users, many=True)
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
    serializer = ImageBoxSerializer(images, many=True)
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
    serializer = VidBoxSerializer(all_vids, many=True)
    return Response(serializer.data)


# live functions
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
    serializer = LiveSerializer(live_now, many=True)
    return Response(serializer.data)


# Notifications
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_user_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).order_by(
        '-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_user_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by(
        '-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_triggered_notifications(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        notification_trigger="Triggered").filter(
        read="Not Read").order_by('-date_created')
    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def read_notification(request):
    notifications = ScheduledNotifications.objects.filter(notification_to=request.user).filter(
        read="Not Read").order_by('-date_created')
    for i in notifications:
        i.read = "Read"
        i.save()

    serializer = ScheduledNotificationSerializer(notifications, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def notification_detail(request, id):
    notification = get_object_or_404(ScheduledNotifications, id=id)
    serializer = ScheduledNotificationSerializer(notification, many=False)
    return Response(serializer.data)
