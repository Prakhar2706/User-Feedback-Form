from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Questions)
admin.site.register(Options)
admin.site.register(CustomerFeedback)
admin.site.register(CustomerResponse)