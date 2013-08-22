# coding: utf-8
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import get_object_or_404
from eventex.core.models import Speaker, Talk


def homepage(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    return render_to_response('index.html', context)

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html',
                  context)

def talk_list(request):
    context = {
        'morning_talks': Talk.objects.at_morning(),
        'afternoon_talks': Talk.objects.at_afternoon(), 
        }
    return render(request, 'core/talk_list.html', context)

def talk_detail(request, pk):
    talk = get_object_or_404(Talk, pk=pk)
    context = {'talk' : talk,
               }
    return render(request, 'core/talk_detail.html', context)
