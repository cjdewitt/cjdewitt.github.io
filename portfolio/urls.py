from django.urls import path
from . import views
from django_distill import distill_path

def get_index():
    return None

urlpatterns = [
    distill_path(
        '',  
        views.home,
        name='home',
        distill_func=get_index,
    ),
    distill_path(
        'page1/',
        views.page1,
        name='page1',
        distill_func=get_index,
    ),
    distill_path(
        'page2/',
        views.page2,
        name='page2',
        distill_func=get_index,
    ),
]
