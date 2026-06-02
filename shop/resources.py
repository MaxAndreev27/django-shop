from django.utils.translation import get_language
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget

from .models import Category, Product


class CategoryResource(resources.ModelResource):
    name_uk = fields.Field(column_name="name_uk")
    slug_uk = fields.Field(column_name="slug_uk")
    name_en = fields.Field(column_name="name_en")
    slug_en = fields.Field(column_name="slug_en")

    class Meta:
        model = Category
        # ОБОВ'ЯЗКОВО додаємо кастомні поля сюди, інакше вони вирізаються при експорті
        fields = ("id", "name_uk", "slug_uk", "name_en", "slug_en")
        export_order = ("id", "name_uk", "slug_uk", "name_en", "slug_en")

    def dehydrate_name_uk(self, instance):
        return instance.safe_translation_getter("name", language_code="uk") or ""

    def dehydrate_slug_uk(self, instance):
        return instance.safe_translation_getter("slug", language_code="uk") or ""

    def dehydrate_name_en(self, instance):
        return instance.safe_translation_getter("name", language_code="en") or ""

    def dehydrate_slug_en(self, instance):
        return instance.safe_translation_getter("slug", language_code="en") or ""

    def save_instance(self, instance, is_create, row, **kwargs):
        current_lang = get_language() or "uk"
        for lang in ["uk", "en"]:
            name = row.get(f"name_{lang}")
            slug = row.get(f"slug_{lang}")

            if not name and lang == current_lang:
                name = row.get("name")
            if not slug and lang == current_lang:
                slug = row.get("slug")

            if name or slug:
                instance.set_current_language(lang)
                if name:
                    instance.name = name
                if slug:
                    instance.slug = slug

        super().save_instance(instance, is_create, row, **kwargs)


class ProductResource(resources.ModelResource):
    category = fields.Field(
        column_name="category_id",
        attribute="category",
        widget=ForeignKeyWidget(Category, "id"),  # type: ignore
    )
    name_uk = fields.Field(column_name="name_uk")
    slug_uk = fields.Field(column_name="slug_uk")
    description_uk = fields.Field(column_name="description_uk")

    name_en = fields.Field(column_name="name_en")
    slug_en = fields.Field(column_name="slug_en")
    description_en = fields.Field(column_name="description_en")

    class Meta:
        model = Product
        # Додаємо всі мовні поля в список дозволених для експорту/імпорту
        fields = (
            "id",
            "category",
            "price",
            "available",
            "name_uk",
            "slug_uk",
            "description_uk",
            "name_en",
            "slug_en",
            "description_en",
        )
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

    def save_instance(self, instance, is_create, row, **kwargs):
        current_lang = get_language() or "uk"
        for lang in ["uk", "en"]:
            name = row.get(f"name_{lang}")
            slug = row.get(f"slug_{lang}")
            description = row.get(f"description_{lang}")

            if not name and lang == current_lang:
                name = row.get("name")
            if not slug and lang == current_lang:
                slug = row.get("slug")
            if not description and lang == current_lang:
                description = row.get("description", "")

            if name or slug or description:
                instance.set_current_language(lang)
                if name:
                    instance.name = name
                if slug:
                    instance.slug = slug
                if description is not None:
                    instance.description = description

        super().save_instance(instance, is_create, row, **kwargs)
