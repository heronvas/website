from django.db import models
from datetime import datetime



class Event(models.Model):
    tutorial_series = models.CharField(max_length=200)
    series_date=models.DateTimeField("date published",default=datetime.now())
    series_slug = models.CharField(max_length=200, default='events')
    
   
    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "events"

    def __str__(self):
        return self.tutorial_series



class Video(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    
    
    tutorial_series = models.ForeignKey(Event, default='events', verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default='events')
    

    def __str__(self):
        return self.title

# Create your models here.
