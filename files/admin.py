from django.contrib import admin
from .models import (
    Client,
    Institution,
    HealthPlan,
    Writing,
)


admin.site.register(Client)
admin.site.register(Institution)
admin.site.register(HealthPlan)
admin.site.register(Writing)
