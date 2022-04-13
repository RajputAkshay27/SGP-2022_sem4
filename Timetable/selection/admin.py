import re
from django.contrib import admin
from .models import faculty, subject, resource
# Register your models here.

admin.site.register(faculty)
admin.site.register(subject)
admin.site.register(resource)

