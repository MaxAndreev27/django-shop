from django.db import models
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from parler.models import TranslatableModel, TranslatedFields


class Category(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        slug=models.SlugField(max_length=200, unique=True),
    )

    class Meta:
        # ordering = ['name']
        # indexes = [
        #     models.Index(fields=['name']),
        # ]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        # 1. Намагається знайти 'name' поточною мовою (uk)
        # 2. Якщо немає — шукає будь-яку іншу наявну мову (any_language=True)
        # 3. Якщо взагалі перекладів немає — повертає безпечний дефолт
        return (
            self.safe_translation_getter("name", any_language=True)
            or f"Category #{self.id}"
        )

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200),
        slug=models.SlugField(max_length=200),
        description=models.TextField(blank=True),
    )
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    image_thumbnail = ImageSpecField(
        source="image",
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 85},
    )

    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ['name']
        indexes = [
            # models.Index(fields=['id', 'slug']),
            # models.Index(fields=['name']),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        # Робимо такий самий захист для продуктів, щоб вони не падали при імпорті
        return (
            self.safe_translation_getter("name", any_language=True)
            or f"Product #{self.id}"
        )

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
