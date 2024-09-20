from django.urls import path
from . import views
from django_distill import distill_path

def get_index():
    return None

urlpatterns = [
    distill_path(
        '',  
        views.index,
        name='index',
        distill_func=get_index,
    ),
    distill_path(
        '',
        views.about,
        name='about',
        distill_func=get_index,
    ),
    distill_path(
        '',
        views.projects,
        name='projects',
        distill_func=get_index,
    ),
]
