from django.contrib import admin

# from eventpro.eventapp.models import Event_Dashboard

# Register your models here.
from .models import *


admin.site.register(banner_event)
