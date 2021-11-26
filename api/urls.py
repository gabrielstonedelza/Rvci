from django.urls import path
from . import views

urlpatterns = [
    path('post_devotion/', views.post_devotion),
    path('get_devotions/', views.get_devotions),
    path('get_user_devotions/', views.get_user_devotions),
    path('devotion_detail/<str:slug>/', views.devotion_detail),
    path('post_prayer/', views.post_prayer),
    path('get_prayers/', views.get_prayer_lists),
    path('get_user_prayers/', views.get_user_prayer_lists),
    path('pray_detail/<str:slug>/', views.prayer_detail),
    path('add_story/', views.add_story),
    path('story_detail/<int:id>/', views.story_detail),
    path('add_event/', views.add_event),
    path('get_current/', views.get_current_event),
    path('event_detail/<str:slug>/', views.event_detail),
    path('add_announcement/', views.add_announcements),
    path('get_current_announcement/', views.get_current_announcement),
    path('announcement_detail/<int:id>/', views.announcement_detail),
    path('comment_devotion/<int:pk>/', views.comment_on_devotion),
    path('devotion_comments/<int:id>/', views.devotion_comments),
    path('comment_detail/<int:id>/', views.comment_detail),
    path('pray_for_user/<int:id>/', views.pray_for_user),
    path('get_pray_for_lists/<int:id>/', views.get_pray_for_lists),
]