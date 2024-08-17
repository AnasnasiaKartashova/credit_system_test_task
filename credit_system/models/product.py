from django.db import models

from credit_system.models.credit_application import CreditApplicationModel
from credit_system.models.maker import MakerModel


class ProductModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    maker = models.ForeignKey(
        MakerModel,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name="Производитель",
    )
    credit_application = models.ForeignKey(
        CreditApplicationModel,
        on_delete=models.CASCADE,
        related_name="product",
        verbose_name="Кредитная заявка",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
