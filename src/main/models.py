from datetime import timezone

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара")
    price = models.PositiveIntegerField(verbose_name="Стоимость товара")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['id']
