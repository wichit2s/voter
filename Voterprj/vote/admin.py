from django.contrib import admin
from vote.models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)