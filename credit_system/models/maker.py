from django.db import models


class MakerModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "maker"
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"
