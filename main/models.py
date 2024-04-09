from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        verbose_name="Название категории товаров",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления")
    is_deleted = models.BooleanField(
        default=False,
        verbose_name="Удалено")
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Slug"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        blank=False,
        verbose_name="Название категории товаров",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, 
        verbose_name="Дата обновления")
    is_deleted = models.BooleanField(
        default=False, 
        verbose_name="Удалено")
    quantity = models.PositiveIntegerField(
        verbose_name="Количество на складе", 
        default=0
    )
    category = models.ForeignKey(
        to=Category, 
        on_delete=models.CASCADE, 
        verbose_name="Категория"
    )
    image = models.ImageField(
        blank=True, null=True, 
        verbose_name="Изображение", 
        upload_to="product_images"
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name="Скидка в процентах"
    )
    params = models.JSONField(
        null=True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        null=True,
        verbose_name="Slug"
    )

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name  # тут можно через ф строку вывести дополнительно
