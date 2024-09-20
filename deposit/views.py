from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from .serializers import DepositSerializer

class DepositCalculationView(APIView):
    """Представление для расчета процентов по вкладу."""

    def post(self, request) -> Response:
        """Обработка POST-запроса для расчета процентов по вкладу.

        Аргументы:
            request: Объект запроса, содержащий данные о вкладе.

        Возвращает:
            Response: Объект ответа с результатами расчета или ошибками валидации.
        """
        serializer = DepositSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            start_date = datetime.strptime(data['date'], "%d.%m.%Y")  
            periods = data['periods']
            amount = data['amount'] 
            rate = data['rate'] / 100 

            result = {}

            for i in range(periods):
                amount += amount * (rate / 12)  # Начисление процентов за месяц
                
                current_date = start_date + timedelta(days=30 * (i + 1))  # Дата через 30 дней
                result[current_date.strftime("%d.%m.%Y")] = round(amount, 2)  # Сохранение результата

            return Response(result, status=status.HTTP_200_OK)
        else:
            error_message = "Описание ошибка"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
