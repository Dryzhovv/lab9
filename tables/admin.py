from django.contrib import admin

# Register your models here.
from tables.models import Plane, Flight


@admin.register(Plane, Flight)
class ModelsAdmin(admin.ModelAdmin):
    pass
