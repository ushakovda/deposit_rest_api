from rest_framework import serializers
from .models import DepositApplication


class DepositSerializer(serializers.ModelSerializer):
    """Сериализатор для данных о вкладе и работы с моделью заявки."""

    class Meta:
        model = DepositApplication
        fields = ["date", "periods", "amount", "rate"]
