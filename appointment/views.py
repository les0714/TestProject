from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from appointment.forms import UserData
from appointment import models


def index_page(request):
    if not request.user.is_authenticated():
        return HttpResponseNotFound(get_template('404.html').render(Context({})))
    return render(request, "index.html", {
        'meetings_data': models.MeetingData.objects.all()
    })

def appointment_page(request):
    if request.POST:
        user_data_form = UserData(request.POST)
        user_data_form, state = user_data_form.process(request)
        if state:
            return HttpResponseRedirect('/appointment/')
    else:
        user_data_form = UserData()


    return render(request, "appointment_page.html", {
        'user_data_form': user_data_form
    })