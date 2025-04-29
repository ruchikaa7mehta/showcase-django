from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.get_projects, name='get_projects'),
    path('projects', views.create_project, name='create_project'),
    path('projects/<int:id>/summary', views.project_summary, name='project_summary'),
]
