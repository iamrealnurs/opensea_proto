import urllib.request
from datetime import timezone
from django.contrib.auth import get_user_model
from django.db import models
from django.core.files import File
import os

User = get_user_model()

class Seller(User):
    blockchain_network_name = models.CharField(max_length=200, verbose_name="Название Сети")
    blockchain_wallet_address = models.CharField(max_length=200, unique=True, verbose_name="Адрес кошелька")

    class Meta:
        verbose_name="Продавец"
        verbose_name_plural = "Продавцы"
        ordering = ['id']

class Product(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара")
    price = models.PositiveIntegerField(verbose_name="Стоимость товара")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    token_id = models.PositiveIntegerField(verbose_name="Token ID", null=True)
    image_file = models.ImageField(upload_to='media', null=True)
    image_url = models.URLField(default="https://picsum.photos/200/200.jpg")

    def __str__(self):
        return self.title

    def get_remote_image(self):
        if self.image_url and not self.image_file:
            result = urllib.request.urlretrieve(self.image_url)
            self.image_file.save(
                os.path.basename(self.image_url),
                File(open(result[0]))
            )
            self.save()

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['id']


