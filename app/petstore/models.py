from django.db import models

# Create your models here.

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
    
    type = models.CharField("Тип",
        max_length=255,
        help_text="Обязательное поле",
        null=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class ProductAmounts(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField("Количество", 
        blank=False,
        null=False,
        help_text="Обязательное поле" )

    def __str__(self) -> str:
        return self.product_id.name

    class Meta:
        verbose_name = 'Количество продукта'
        verbose_name_plural = 'Количества продуктов'
