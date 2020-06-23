from django.contrib import admin
from .models import Event
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Video




class VideoAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("Title", {'fields': ["title"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {'fields': ["content"]}),
        
        
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},

        }

admin.site.register(Event)

admin.site.register(Video,VideoAdmin)
# Register your models here.
