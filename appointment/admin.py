from django.contrib import admin

from appointment import models

admin.site.register(models.MeetingDate)
admin.site.register(models.MeetingTime)
admin.site.register(models.MeetingData)