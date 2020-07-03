from django.contrib import admin
from . import models
"""Register models with admin site"""
admin.site.register(models.Member)              # Register Member model
admin.site.register(models.ActivityPeriods)     # Register ActivityPeriod model
