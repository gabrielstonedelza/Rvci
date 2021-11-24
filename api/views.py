from django.shortcuts import get_object_or_404
from .models import  Devotion,PrayerList,Stories,Events,Announcements,Likes,Comments,PrayFor,NotifyMe
from .serializers import DevotionSerializer,PrayerListSerializer,StoriesSerializer,EventsSerializer,LikesSerializer,CommentsSerializer,PrayforSerializer,NotifymeSerializer,AnnouncementSerializer
from datetime import datetime,date,time,timedelta

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
def devotion_detail(request,id):
    devotion = get_object_or_404(Devotion,id=id)
    serializer = DevotionSerializer(devotion,many=False)
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
def prayer_detail(request,id):
    prayer = get_object_or_404(PrayerList,id=id)
    serializer = PrayerListSerializer(prayer,many=False)
    return Response(serializer.data)

# post new story
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_story(request):
    serializer = StoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# story detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def story_detail(request, id):
    story = get_object_or_404(Stories, id=id)
    serializer = StoriesSerializer(story, many=False)
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
def event_detail(request,id):
    event = get_object_or_404(Events,id=id)
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

# add like to devotion
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_devotion(request,id):
    devotion = get_object_or_404(Devotion,id=id)
    serializer = LikesSerializer(devotion,data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get devotion likes
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def devotion_likes(request,id):
    devotion = get_object_or_404(Devotion,id=id)
    likes = Likes.objects.filter(devotion=devotion).order_by('-date_liked')
    serializer = LikesSerializer(likes,many=True)
    return Response(serializer.data)

# like detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def likes_detail(request,id):
    like = get_object_or_404(Likes,id=id)
    serializer = LikesSerializer(like,many=False)
    return Response(serializer.data)

# posting devotional comments
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def comment_on_devotion(request,id):
    devotion = get_object_or_404(Devotion, id=id)
    serializer = CommentsSerializer(devotion,data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get devotion comments
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def devotion_comments(request,id):
    devotion = get_object_or_404(Devotion, id=id)
    serializer = CommentsSerializer(devotion,many=True)
    return Response(serializer.data)

# comment detail
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def comment_detail(request,id):
    comment = get_object_or_404(Comments,id=id)
    serializer = CommentsSerializer(comment,many=False)
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
