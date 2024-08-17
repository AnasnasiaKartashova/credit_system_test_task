from django.db import models
from credit_system.models.contract import ContractModel


class CreditApplicationModel(models.Model):
    contract = models.OneToOneField(
        ContractModel,
        on_delete=models.CASCADE,
        related_name="credit_application",
        verbose_name="Контракт",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"№{self.id}"

    class Meta:
        db_table = "credit_application"
        verbose_name = "Кредитная заявка"
        verbose_name_plural = "Кредитные заявки"
