from django.contrib import admin
from import_export.admin import ImportExportMixin
from parler.admin import TranslatableAdmin

from .models import Category, Product
from .resources import CategoryResource, ProductResource


@admin.register(Category)
class CategoryAdmin(ImportExportMixin, TranslatableAdmin):
    resource_classes = [CategoryResource]
    list_display = ["name", "slug"]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(ImportExportMixin, TranslatableAdmin):
    resource_classes = [ProductResource]
    list_display = ["name", "slug", "price", "available", "created", "updated"]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available"]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}
