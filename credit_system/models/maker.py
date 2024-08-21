from django.db import models
from credit_system.mixin_models.created_at_mixin_model import CreatedAtMixin


class MakerModel(CreatedAtMixin, models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "maker"
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
