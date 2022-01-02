from django.contrib import admin
from .models import (Devotion, PrayerList, Events, Announcements, PrayFor,DailyVids, ImageBoxes,VidBoxes,LiveNow,Stories)

admin.site.register(Devotion)
admin.site.register(PrayerList)
admin.site.register(Events)
admin.site.register(Announcements)
admin.site.register(PrayFor)
admin.site.register(ImageBoxes)
admin.site.register(VidBoxes)
admin.site.register(LiveNow)
admin.site.register(Stories)
admin.site.register(DailyVids)
