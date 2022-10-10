# Generated by Django 4.1 on 2022-10-10 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Обязательное поле', max_length=255, unique=True, verbose_name='Название')),
                ('price', models.FloatField(default=500, help_text='Обязательное поле', max_length=255, verbose_name='Цена')),
                ('description', models.TextField(blank=True, default='Empty', max_length=255, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Обязательное поле', max_length=255, verbose_name='Тип продукта')),
            ],
            options={
                'verbose_name': 'Тип продукта',
                'verbose_name_plural': 'Типы продуктов',
            },
        ),
        migrations.CreateModel(
            name='ProductAmounts',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='petstore.product')),
                ('amount', models.IntegerField(help_text='Обязательное поле', verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Количество продукта',
                'verbose_name_plural': 'Количества продуктов',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(help_text='Обязательное поле', max_length=255, on_delete=django.db.models.deletion.CASCADE, to='petstore.producttype'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Оплачено'), (1, 'Ожидание'), (2, 'Отмена')], default=1)),
                ('products', models.ManyToManyField(to='petstore.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзины',
                'ordering': ('-created_at',),
            },
        ),
    ]
