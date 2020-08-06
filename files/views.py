from django.http import HttpResponse
from django.shortcuts import render
from files.models import (
    Client,
    Institution,
    HealthPlan,
)


def  get_info(request):
    clients = Client.objects.all()
    import pdb; pdb.set_trace()
    institutions = Institution.objects.all()
    health_plans = HealthPlan.objects.all()
    context = {
        'clients': clients,
        'institutions': institutions,
        'health_plans': health_plans,
    }

    return render(request, 'files/index.html', context)