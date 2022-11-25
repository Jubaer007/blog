from django.urls import path
from websites import views

urlpatterns = [
    path('index', views.index, name='index')
]
