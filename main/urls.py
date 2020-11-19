from django.urls import path

from . import views
from django.views.generic.base import TemplateView

app_name ='app'

urlpatterns = [
    path('', views.main, name = 'main'),
]