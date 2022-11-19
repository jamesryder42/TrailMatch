from django.contrib import admin

# Register your models here.
from .models import Trail,User
admin.site.register(Trail)
admin.site.register(User)
