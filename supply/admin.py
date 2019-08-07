from django.contrib import admin

# Register your models here.

from supply.models import Distillate
from supply.models import Cartridge
from supply.models import Batch
from supply.models import Battery


class DistillateAdmin(admin.ModelAdmin):
    list_display = ["name"]


class CartridgeAdmin(admin.ModelAdmin):
    list_display = ["name"]


class BatchAdmin(admin.ModelAdmin):
    list_display = ["batch_name"]


class BatteryAdmin(admin.ModelAdmin):
    list_display = ["battery_name"]


admin.site.register(Distillate, DistillateAdmin)
admin.site.register(Cartridge, CartridgeAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Battery, BatteryAdmin)
