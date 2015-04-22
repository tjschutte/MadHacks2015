from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from datetime import datetime, timedelta
from django.utils import timezone
from .models import Event
import quickstart
#import quickstart

# Create your views here.


def index(request):
    now = datetime.now().date()
    temp = now
    weeks = []
    dayOfWeek = now.weekday()
    if(dayOfWeek != 6):
        temp = temp - timedelta(days=dayOfWeek + 1)
    eventsAll = []
    events = Event.objects.all()
##    try:
##        eventsAll.extend(quickstart.GetEvents())
##    except deleted_client:
##        print "Could not get user's events from google"
    for e in eventsAll:
        print e.title
    eventsAll.extend(events)
    for e in eventsAll:
        print e.title
    r =0
    while(r < 4):
        days = []
        x = 0
        while(x < 7):
            days.append(temp)
            x += 1
            temp = temp + timedelta(days=1)
        r += 1
        weeks.append(days)
    return render(request, 'taskmaster/index.html', {'events': eventsAll, 'now': now.strftime('%B'), 'weeks': weeks})
