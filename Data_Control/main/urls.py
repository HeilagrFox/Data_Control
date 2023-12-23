from . import views
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('faculty', views.get_entrants_by_faculty),
    path('marks', views.marks)
]