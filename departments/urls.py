from django.urls import path
from departments import views

urlpatterns = [
    path('departments', views.Departments.as_view())
]