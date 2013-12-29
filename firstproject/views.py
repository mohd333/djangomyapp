from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template
import datetime

def hello(request):
    return HttpResponse("helloworld")

def current_time(request):
    now = datetime.datetime.now()
    return render(request, 'first_template.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'additional_time.html', {'index': offset, 'addtime': dt})


# Create your views here.
