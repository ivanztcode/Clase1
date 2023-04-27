from django.urls import path, include
from alumno import views


urlpatterns = [
    path("", views.homeAlumno, name="alumnoHome")
]
