from django.contrib import admin
from .models import *


admin.site.register(Record)
admin.site.site_header = 'Coffeevar'