from django.urls import path
from . import views

urlpatterns = [
    path('post_devotion/', views.post_devotion),
    path('post_story/', views.post_stories),
    path('get_devotions/', views.get_devotions),
    path('get_stories/', views.get_stories),
    path('get_user_stories/<int:pk>/', views.get_user_stories),
    path('get_user_devotions/', views.get_user_devotions),
    path('devotion_detail/<str:slug>/', views.devotion_detail),
    path('post_prayer/', views.post_prayer),
    path('get_prayers/', views.get_prayer_lists),
    path('get_user_prayers/', views.get_user_prayer_lists),
    path('pray_detail/<str:slug>/', views.prayer_detail),
    path('add_event/', views.add_event),
    path('get_current/', views.get_current_event),
    path('event_detail/<str:slug>/', views.event_detail),
    path('add_announcement/', views.add_announcements),
    path('get_current_announcement/', views.get_current_announcement),
    path('announcement_detail/<int:id>/', views.announcement_detail),

    path('pray_for_user/<int:id>/', views.pray_for_user),
    path('get_pray_for_lists/<int:id>/', views.get_pray_for_lists),

    path('get_all_users/', views.get_all_users),

    path('add_to_images/', views.add_to_images),
    path('add_to_vids/',views.add_to_vids),
    path("get_images/",views.get_all_images),
    path('get_vids/', views.get_all_videos),

    path('post_live/', views.add_live),
    path('get_live/', views.get_live_now)
]