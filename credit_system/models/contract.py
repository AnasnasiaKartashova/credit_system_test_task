from django.db import models
from credit_system.mixin_models.created_at_mixin_model import CreatedAtMixin


class ContractModel(CreatedAtMixin, models.Model):
    description = models.CharField(
        max_length=4048, verbose_name="Дополнительные сведения"
    )

    def __str__(self):
        return f"№{self.id}"

    class Meta:
        db_table = "contract"
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
