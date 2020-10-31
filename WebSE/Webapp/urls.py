from Webapp import views
from django.urls import path

urlpatterns = [
    path('',views.index, name="Webapp"),
    path('fddonate',views.FoodDonationView),
]
