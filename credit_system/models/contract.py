from django.db import models


class ContractModel(models.Model):
    description = models.CharField(
        max_length=4048, verbose_name="Дополнительные сведения"
    )
    file_url = models.CharField(max_length=4048, verbose_name="Ссылка на документ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"№{self.id}"

    class Meta:
        db_table = "contract"
        verbose_name = "Контракт"
        verbose_name_plural = "Контракты"
