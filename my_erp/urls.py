from django.urls import path
from . import views

urlpatterns = [
    path('', views.table_list, name='table_list'),
]