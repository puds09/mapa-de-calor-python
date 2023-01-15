# from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path("form/", views.heat_form),
    path("getData/", views.get_data, name="getData"),
    path("renderMap/", views.render_map, name="renderMap"),
]
