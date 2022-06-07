# from email.policy import default
# from tokenize import blank_re
# from django.db import models

# Create your models here.

from dataclasses import make_dataclass
from distutils.command.upload import upload
from django.db import models


#Model to upload banner seasonal events

class banner_event(models.Model):
    banner_event_name = models.CharField(max_length=100)
    banner_event_image = models.ImageField(upload_to='banner_event_media', blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.banner_event_name


