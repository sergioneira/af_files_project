from django.urls import path
from .views import (
    get_info,
    get_writing,
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
        name="writing",
    )
]
