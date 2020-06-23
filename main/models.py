from django.db import models
from datetime import datetime



class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    series_date=models.DateTimeField("date published",default=datetime.now())
    series_slug = models.CharField(max_length=200, default='series')
    series_summary = models.CharField(max_length=200)
   
    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "series"

    def __str__(self):
        return self.tutorial_series



class Disco(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    date=models.DateTimeField("date published",default=datetime.now())
    
    tutorial_series = models.ForeignKey(TutorialSeries, default='series', verbose_name="Series", on_delete=models.SET_DEFAULT)
    tutorial_slug = models.CharField(max_length=200, default='series')
    

    def __str__(self):
        return self.title


class Uploads(models.Model):
    file =  models.FileField(max_length=140, default='')

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Uploads"
    

# Create your models here.
