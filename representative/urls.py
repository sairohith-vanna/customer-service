from django.urls import path
from representative import views

urlpatterns = [
    path('representative', views.RepresentativeDetail.as_view()),
    path('representative/<str:rep_id>', views.RepresentativeDetails.as_view())
]