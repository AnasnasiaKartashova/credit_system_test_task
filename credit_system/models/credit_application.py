from django.db import models
from credit_system.mixin_models.created_at_mixin_model import CreatedAtMixin
from credit_system.models.contract import ContractModel


class CreditApplicationModel(CreatedAtMixin, models.Model):
    contract = models.OneToOneField(
        ContractModel,
        on_delete=models.CASCADE,
        related_name="credit_application",
        verbose_name="Контракт",
    )

    def __str__(self):
        return f"№{self.id}"

    class Meta:
        db_table = "credit_application"
        verbose_name = "Кредитная заявка"
        verbose_name_plural = "Кредитные заявки"
