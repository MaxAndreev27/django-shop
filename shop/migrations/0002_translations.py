import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        # 1. СПОЧАТКУ ВИДАЛЯЄМО ІНДЕКСИ (бо вони посилаються на старі поля)
        migrations.RemoveIndex(
            model_name="category",
            name="shop_catego_name_289c7e_idx",
        ),
        migrations.RemoveIndex(
            model_name="product",
            name="shop_produc_id_f21274_idx",
        ),
        migrations.RemoveIndex(
            model_name="product",
            name="shop_produc_name_a2070e_idx",
        ),
        # 2. ОНОВЛЮЄМО ОПЦІЇ МОДЕЛЕЙ (прибираємо ordering по полю 'name')
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={},
        ),
        # 3. ТЕПЕР ВИДАЛЯЄМО СТАРІ ПОЛЯ (звільняємо імена 'name', 'slug', 'description')
        migrations.RemoveField(
            model_name="category",
            name="name",
        ),
        migrations.RemoveField(
            model_name="category",
            name="slug",
        ),
        migrations.RemoveField(
            model_name="product",
            name="description",
        ),
        migrations.RemoveField(
            model_name="product",
            name="name",
        ),
        migrations.RemoveField(
            model_name="product",
            name="slug",
        ),
        # 4. СТВОРЮЄМО МОДЕЛІ ПЕРЕКЛАДІВ
        migrations.CreateModel(
            name="CategoryTranslation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "category Translation",
                "db_table": "shop_category_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatableModel, models.Model),
        ),
        migrations.CreateModel(
            name="ProductTranslation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "language_code",
                    models.CharField(
                        db_index=True, max_length=15, verbose_name="Language"
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200)),
                ("description", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "product Translation",
                "db_table": "shop_product_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        # 5. ЗВ'ЯЗУЄМО ТАБЛИЦІ ПЕРЕКЛАДІВ З БАЗОВИМИ МОДЕЛЯМИ ЧЕРЕЗ MASTER
        # (тепер конфлікту імен не буде, бо поля name/slug з кроку 3 вже видалені!)
        migrations.AddField(
            model_name="categorytranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="shop.category",
            ),
        ),
        migrations.AddField(
            model_name="producttranslation",
            name="master",
            field=parler.fields.TranslationsForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="translations",
                to="shop.product",
            ),
        ),
        # 6. ДОДАЄМО УНІКАЛЬНІ КОНСТРЕЙНТИ ДЛЯ МОВ
        migrations.AddConstraint(
            model_name="categorytranslation",
            constraint=models.UniqueConstraint(
                fields=("language_code", "master"),
                name="shop_category_translation_uniq_lang",
            ),
        ),
        migrations.AddConstraint(
            model_name="producttranslation",
            constraint=models.UniqueConstraint(
                fields=("language_code", "master"),
                name="shop_product_translation_uniq_lang",
            ),
        ),
    ]
