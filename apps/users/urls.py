from django.urls import path
from . import views

urlpatterns = [
    path('sahil/',views.show_name,name='show_name'),
]