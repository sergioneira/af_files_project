from django.contrib import admin
from .models import (
    Client,
    Institution,
    HealthPlan,
)


class ClientAdmin(admin.ModelAdmin):
    pass


class InstitutionAdmin(admin.ModelAdmin):
    pass


class HealthPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(HealthPlan, HealthPlanAdmin)
