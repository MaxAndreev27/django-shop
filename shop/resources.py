from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Category, Product


class CategoryResource(resources.ModelResource):
    # Явно оголошуємо колонки для кожної мови
    name_uk = fields.Field(column_name="name_uk")
    slug_uk = fields.Field(column_name="slug_uk")
    name_en = fields.Field(column_name="name_en")
    slug_en = fields.Field(column_name="slug_en")

    class Meta:
        model = Category
        fields = ("id",)
        export_order = ("id", "name_uk", "slug_uk", "name_en", "slug_en")

    # Логіка Експорту: дістаємо переклади безпечно
    def dehydrate_name_uk(self, instance):
        return instance.safe_translation_getter("name", language_code="uk") or ""

    def dehydrate_slug_uk(self, instance):
        return instance.safe_translation_getter("slug", language_code="uk") or ""

    def dehydrate_name_en(self, instance):
        return instance.safe_translation_getter("name", language_code="en") or ""

    def dehydrate_slug_en(self, instance):
        return instance.safe_translation_getter("slug", language_code="en") or ""

    # Логіка Імпорту: розкладаємо дані з CSV по таблицях перекладів
    def save_instance(self, instance, is_create, row, **kwargs):
        # Передаємо точно 3 аргументи, а решту прокидуємо через **kwargs
        super().save_instance(instance, is_create, row, **kwargs)
        for lang in ["uk", "en"]:
            name = row.get(f"name_{lang}")
            slug = row.get(f"slug_{lang}")
            if name or slug:
                instance.set_current_language(lang)
                instance.name = name
                instance.slug = slug
                instance.save()


class ProductResource(resources.ModelResource):
    # Зв'язок з категорією через ID (так надійніше для імпорту)
    category = fields.Field(
        column_name="category_id",
        attribute="category",
        widget=ForeignKeyWidget(Category, "id"),  # type: ignore
    )
    # Поля перекладів для Product
    name_uk = fields.Field(column_name="name_uk")
    slug_uk = fields.Field(column_name="slug_uk")
    description_uk = fields.Field(column_name="description_uk")

    name_en = fields.Field(column_name="name_en")
    slug_en = fields.Field(column_name="slug_en")
    description_en = fields.Field(column_name="description_en")

    class Meta:
        model = Product
        fields = ("id", "category", "price", "available")
        export_order = (
            "id",
            "category_id",
            "price",
            "available",
            "name_uk",
            "slug_uk",
            "description_uk",
            "name_en",
            "slug_en",
            "description_en",
        )

    # Логіка Експорту продуктів
    def dehydrate_name_uk(self, instance):
        return instance.safe_translation_getter("name", language_code="uk") or ""

    def dehydrate_slug_uk(self, instance):
        return instance.safe_translation_getter("slug", language_code="uk") or ""

    def dehydrate_description_uk(self, instance):
        return instance.safe_translation_getter("description", language_code="uk") or ""

    def dehydrate_name_en(self, instance):
        return instance.safe_translation_getter("name", language_code="en") or ""

    def dehydrate_slug_en(self, instance):
        return instance.safe_translation_getter("slug", language_code="en") or ""

    def dehydrate_description_en(self, instance):
        return instance.safe_translation_getter("description", language_code="en") or ""

    # Логіка Імпорту продуктів
    def save_instance(self, instance, is_create, row, **kwargs):
        # Передаємо точно 3 аргументи, а решту прокидуємо через **kwargs
        super().save_instance(instance, is_create, row, **kwargs)
        # Потім створюємо/оновлюємо переклади
        for lang in ["uk", "en"]:
            name = row.get(f"name_{lang}")
            slug = row.get(f"slug_{lang}")
            description = row.get(f"description_{lang}", "")
            if name or slug:
                instance.set_current_language(lang)
                instance.name = name
                instance.slug = slug
                instance.description = description
                instance.save()
