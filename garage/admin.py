from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Car)
admin.site.register(models.Service)
admin.site.register(models.Employee)
admin.site.register(models.Department)
admin.site.register(models.History)
