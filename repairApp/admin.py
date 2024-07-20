from django.contrib import admin

from repairApp.models import Manufacturer, Car, WorkShop, ManufacturerWorkShop, Repair


# Register your models here.

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False
admin.site.register(Manufacturer, ManufacturerAdmin)
class CarAdmin(admin.ModelAdmin):
    list_display = ('type', 'maxSpeed')
admin.site.register(Car, CarAdmin)
class ManufacturerWorkShopInline(admin.StackedInline):
    model = ManufacturerWorkShop
    extra = 1
class WorkShopAdmin(admin.ModelAdmin):
    inlines = [ManufacturerWorkShopInline,]
admin.site.register(WorkShop, WorkShopAdmin)

class RepairAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
admin.site.register(Repair, RepairAdmin)