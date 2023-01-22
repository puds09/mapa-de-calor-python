from django.urls import path, include
from . import views

urlpatterns = [
    path("form/", views.heat_form, name="form"),
    path("getData/", views.get_data, name="getData"),
    path("modalMap", views.modal_mapa, name="modalMap"),
]
