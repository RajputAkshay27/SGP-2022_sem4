import re
from django.contrib import admin
from .models import faculty, subject, resource,priority
# Register your models here.

admin.site.register(faculty)
admin.site.register(subject)
admin.site.register(resource)
admin.site.register(priority)