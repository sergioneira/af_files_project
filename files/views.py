import json

from django.http import HttpResponse
from django.shortcuts import (
    get_object_or_404,
    render,
)
from files.models import (
    Client,
    Institution,
    HealthPlan,
    Writing,
)


def get_info(request):
    clients = Client.objects.all()
    institutions = Institution.objects.all()
    health_plans = HealthPlan.objects.all()
    context = {
        'clients': clients,
        'institutions': institutions,
        'health_plans': health_plans,
    }

    return render(request, 'files/index.html', context)


def get_writing(request):
    content = Writing.objects.first().content
    return HttpResponse(content)


def get_client_info(request, run_client):
    client = get_object_or_404(Client, run=run_client)
    serialized_client = json.dumps(client.__str__())
    return HttpResponse(serialized_client, 'application/json')

def get_institution_info(request, rut_institution):
    institution = get_object_or_404(Institution, rut=rut_institution)
    serialized_institution = json.dumps(institution.__str__())
    return HttpResponse(serialized_institution, 'application/json')
    