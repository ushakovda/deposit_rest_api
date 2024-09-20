from rest_framework import serializers

class DepositSerializer(serializers.Serializer):
    """Сериализатор для данных о вкладе."""

    date: str = serializers.CharField() 
    periods: int = serializers.IntegerField(min_value=1, max_value=60)
    amount: int = serializers.IntegerField(min_value=10000, max_value=3000000)
    rate: float = serializers.FloatField(min_value=1, max_value=8)
