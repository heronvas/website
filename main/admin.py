from django.contrib import admin
from .models import Disco
from tinymce.widgets import TinyMCE
from django.db import models
from .models import TutorialSeries
from .models import Uploads




class DiscoAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("Title/date", {'fields': ["title", "date"]}),
        ("URL", {'fields': ["tutorial_slug"]}),
        ("Series", {'fields': ["tutorial_series"]}),
        ("Content", {"fields": ["content"]}),

    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},

        }


class UploadsAdmin(admin.ModelAdmin):
    
    fieldsets = [
        
        ("file upload", {"fields" : ["file"]})
    ]

admin.site.register(TutorialSeries)
admin.site.register(Uploads, UploadsAdmin)

admin.site.register(Disco,DiscoAdmin)
# Register your models here.
