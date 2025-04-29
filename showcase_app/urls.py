from django.urls import path
from . import views

urlpatterns = [
    path('api/projects', views.project_list, name='project_list'),
    path('api/projects/<int:pk>/summary', views.project_summary),
]
