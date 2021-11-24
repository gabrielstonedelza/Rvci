from django.shortcuts import get_object_or_404
from .models import User, Profile
from .serializers import UsersSerializer, ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from drf_multiple_model.views import ObjectMultipleModelAPIView

# Create your views here.
def rvci_home(request):
    return render(request, "users/rvci_home.html")


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile(request):
    my_profile = Profile.objects.filter(user=request.user)
    serializer = ProfileSerializer(my_profile, many=True)
    return Response(serializer.data)
    
@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_profile(request):
    my_profile = Profile.objects.get(user=request.user)
    serializer = ProfileSerializer(my_profile, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_username(request):
    user = User.objects.get(username=request.user.username)
    serializer = UsersSerializer(user,data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)