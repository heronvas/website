from django.shortcuts import render
from django.http import HttpResponse
from .models import Event, Video


def single_slug(request, single_slug):

    series=[s.tutorial_slug for s in Video.objects.all()]
    if single_slug in series:
        this_tutorial = Video.objects.get(tutorial_slug=single_slug)

        return render(request,
                      template_name='events/video.html',
                      context = {"tutorial":this_tutorial})


    return HttpResponse("{single slug} chut")




def event(request):
    return render(request, template_name="events/head.html", context={"series":Event.objects.all})
# Create your views here.
