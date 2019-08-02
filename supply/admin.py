from django.contrib import admin

# Register your models here.

from supply.models import Distillate
from supply.models import Cartridge
from supply.models import Batch


class DistillateAdmin(admin.ModelAdmin):
    list_display = ["name"]


class CartridgeAdmin(admin.ModelAdmin):
    list_display = ["name"]


class BatchAdmin(admin.ModelAdmin):
    list_display = ["batch_name"]


admin.site.register(Distillate, DistillateAdmin)
admin.site.register(Cartridge, CartridgeAdmin)
admin.site.register(Batch, BatchAdmin)