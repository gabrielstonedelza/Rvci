from django.contrib import admin
from .models import (DailyDevotion, PrayerRequest, Events, Announcements, Testimonies, ImageBoxes, VidBoxes, LiveNow, Stories, Notifications,)

admin.site.register(Notifications)
admin.site.register(DailyDevotion)
admin.site.register(PrayerRequest)
admin.site.register(Events)
admin.site.register(Announcements)
admin.site.register(Testimonies)
admin.site.register(ImageBoxes)
admin.site.register(VidBoxes)
admin.site.register(LiveNow)
admin.site.register(Stories)

