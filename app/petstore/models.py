from django.db import models

# Create your models here.

class ProductType(models.Model):
    type = models.CharField("Тип продукта", 
        max_length=255,
        help_text="Обязательное поле",
        null=False)

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField("Количество", 
        blank=False,
        null=False,
        help_text="Обязательное поле" )

    def __str__(self) -> str:
        return self.product.name

    class Meta:
        verbose_name = 'Количество продукта'
        verbose_name_plural = 'Количества продуктов'