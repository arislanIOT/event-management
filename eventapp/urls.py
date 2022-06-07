from . import views
from django.urls import path
from .views import *
app_name = "eventapp"

urlpatterns = [
    # path('', views.home_page, name="home_page"),
    path('', views.banner_view, name="home"),
   
]