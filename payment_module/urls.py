from django.urls import path
from .views import confirmpayment

urlpatterns = [
    path('checkout/<slug:slug>', confirmpayment),
]