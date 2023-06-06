from django.shortcuts import render

# Create your views here.

from .models import *

from django.views.generic import ListView

# class MyView(ListView):
#     model = Me
#     public_html_name = 'index.html'
#     context_object_name = 'I am'

def index(request):
    me = Me.objects.all()
    portfolio = Portfolio.objects.all()
    statistic = Statistic.objects.all()
    social =  Social.objects.all()
    context = {
        'Me':me,
        'Portfolio':portfolio,
        'Statistic':statistic,
        'Social':social,
    }
    return render(request, "index.html", context)





