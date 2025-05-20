from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landingPage'), # Home page
    path('day/<str:day>/', views.day_view, name='day'), # Dynamic URL for each day
]