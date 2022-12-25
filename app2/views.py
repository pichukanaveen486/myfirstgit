from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hemanth(request):
    return HttpResponse('<marquee><h2>Vachadandi puggadu...!</h2></marquee>')
    