from django.db import models


class DepositApplication(models.Model):
    """Модель для хранения заявок на расчет депозита."""

    date = models.CharField(max_length=10)
    periods = models.IntegerField()
    amount = models.IntegerField()
    rate = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(periods__gte=1, periods__lte=60), name="periods_range"
            ),
            models.CheckConstraint(
                check=models.Q(amount__gte=10000, amount__lte=3000000),
                name="amount_range",
            ),
            models.CheckConstraint(
                check=models.Q(rate__gte=1.0, rate__lte=8.0), name="rate_range"
            ),
        ]

    def __str__(self):
        return f"Заявка на сумму {self.amount} сроком {self.periods} месяцев"
