from django.urls import path
from . import views

urlPatterns =[
    path('projects_register/', views.register_project, name='register_project'),
]