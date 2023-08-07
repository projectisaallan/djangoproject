from django.contrib import admin
from .models import Video,Audio,Note,MediaFile
# Register your models here.
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Note)
admin.site.register(MediaFile)