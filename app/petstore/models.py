from django.db import models
from django.urls import reverse
from users.models import User
# Create your models here.

class ProductType(models.Model):
    type = models.CharField("Тип продукта", 
        max_length=255,
        help_text="Обязательное поле",
        null=False)

    def get_absolute_url(self):
        return reverse("products-page", kwargs={"type": self.type})
    
    def __str__(self) -> str:
        return self.type
    
    class Meta:
        verbose_name = 'Тип продукта'
        verbose_name_plural = 'Типы продуктов'

class Product(models.Model):
    name = models.CharField("Название",
        unique=True,
        max_length=255,
        null=False,
        help_text="Обязательное поле",
        blank=False)

    price = models.FloatField("Цена",
        max_length=255,
        blank=False,
        help_text="Обязательное поле",
        default=500)

    description = models.TextField("Описание",
        max_length=255,
        blank=True,
        default="Empty")
    
    type = models.ForeignKey(ProductType,
        on_delete=models.CASCADE,
        max_length=255,
        help_text="Обязательное поле",
        null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductAmounts(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key = True)
    amount = models.IntegerField("Количество", 
        blank=False,
        null=False,
        help_text="Обязательное поле" )

    def __str__(self) -> str:
        return self.product.name

    class Meta:
        verbose_name = 'Количество продукта'
        verbose_name_plural = 'Количества продуктов'


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    products = models.ManyToManyField(Product)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    ORDER_STATUS = ((0, 'Оплачено'), (1, 'Ожидание'), (2, 'Отмена'))
    status = models.PositiveSmallIntegerField(choices=ORDER_STATUS)

    def count_total_price(self):
        return 5
    total_price = property(count_total_price)



    def __str__(self):
        return "Корзина " + str(self.user)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'
    