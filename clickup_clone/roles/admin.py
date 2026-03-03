
from django.contrib import admin
from .models import Role, Permission

# Simple registration
admin.site.register(Role)
admin.site.register(Permission)