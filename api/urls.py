from django.urls import path
from . import views

urlpatterns = [
    path("", views.getRoutes, name="routes"),
    path("notes/", views.getNotes, name="notes"),
    # name 'id' need to be the same name as parameter in getNote
    path("notes/<str:id>/", views.getNote, name="note"),
]
