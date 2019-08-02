from django.contrib import admin

# Register your models here.

from supply.models import Distillate


class DistillateAdmin(admin.ModelAdmin):
    list_display = ["name"]


admin.site.register(Distillate, DistillateAdmin)
