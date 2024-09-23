from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path('place-order/', views.place_order, name='place_order'),
]