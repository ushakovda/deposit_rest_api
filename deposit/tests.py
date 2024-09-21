from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class DepositCalculationViewTests(TestCase):
    def setUp(self):
        """Настройка тестового клиента и URL."""
        self.client = APIClient()
        self.url = reverse('deposit-calculation')

    def test_validation_error(self):
        """Тестирование обработки ошибки валидации."""
        response = self.client.post(self.url, {
            "date": "31.02.2021",  # Неверная дата - в феврале 28 дней
            "periods": 3,
            "amount": 100000,
            "rate": 6
        })
        self.assertEqual(response.status_code, 400)  # Ожидаем, что статус будет 400 Bad Request

    def test_boundary_values(self):
        """Тестирование обработки граничных значений."""
        response = self.client.post(self.url, {
            "date": "31.01.2021",
            "periods": 60,  # Максимальное значение
            "amount": 3000000,  # Максимальное значение
            "rate": 8  # Максимальное значение
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 60)  # Ожидаем 60 записей в ответе

    def test_missing_required_fields(self):
        """Тестирование отсутствия данных."""
        response = self.client.post(self.url, {
            "periods": 3,
            "amount": 100000,
            "rate": 6
        })  # Отсутствует поле date
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.data)

        response = self.client.post(self.url, {
            "date": "31.01.2021",
            "periods": 3,
            "rate": 6
        })  # Отсутствует поле amount
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.data)

    def test_invalid_data_types(self):
        """Тестирование неправильных типов данных."""
        response = self.client.post(self.url, {
            "date": "31.01.2021",
            "periods": "three",  # Неправильный тип данных - строка
            "amount": 100000,
            "rate": 6
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.data)

        response = self.client.post(self.url, {
            "date": "31.01.2021",
            "periods": 3,
            "amount": "one hundred thousand",  # Неправильный тип данных
            "rate": 6
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.data)
