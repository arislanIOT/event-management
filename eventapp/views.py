# from msilib.schema import ListView
from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .form import NameForm
# Create your views here.
from eventapp.models import banner_event
from django.views.generic import ListView

def home_page(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "eventapp/homepage.html")



def banner_view(request):
    banner_img = banner_event.objects.all()
    context = {'banner_img': banner_img}
    return render(request, "eventapp/homepage.html", context)

    