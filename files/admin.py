from django.contrib import admin
from .models import (
    Client,
    Institution,
    HealthPlan,
)


admin.site.register(Client)
admin.site.register(Institution)
admin.site.register(HealthPlan)
