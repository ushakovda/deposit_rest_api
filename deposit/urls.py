from django.urls import path
from .views import DepositCalculationView

urlpatterns = [
    path('calculate/', DepositCalculationView.as_view(), name='deposit-calculation'),
]
