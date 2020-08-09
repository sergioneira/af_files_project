from django.urls import path
from .views import (
    get_info,
    get_writing,
    get_client_info,
    get_institution_info,
)


urlpatterns = [
    path(
        '',
        get_info,
        name="",
    ),
    path(
        'writing/',
        get_writing,
        name='writing',
    ),
    path(
        'client/<str:run_client>/',
        get_client_info,
        name='client-info',
    ),
    path(
        'institution/<str:rut_institution>/',
        get_institution_info,
        name='institution-info',
    )
]
