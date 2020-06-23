from django.shortcuts import render
from django.http import HttpResponse
from .models import Disco, TutorialSeries


def single_slug(request, single_slug):

    series=[s.tutorial_slug for s in Disco.objects.all()]
    if single_slug in series:
        this_tutorial = Disco.objects.get(tutorial_slug=single_slug)

        return render(request,
                      template_name='main/info.html',
                      context = {"tutorial":this_tutorial})


    return HttpResponse("{single slug} chut")




def homepage(request):
    return render(request, template_name="main/basic.html", context={"series":TutorialSeries.objects.all})
# Create your views here.
