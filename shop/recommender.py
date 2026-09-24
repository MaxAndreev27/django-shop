from typing import Any, cast

import redis
from django.conf import settings

from .models import Product

# connect to redis
r = redis.from_url(settings.REDIS_URL)


class Recommender:
    def get_product_key(self, product_id: int) -> str:
        return f"product:{product_id}:purchased_with"

    def products_bought(self, products: list[Product]) -> None:
        product_ids = [p.id for p in products]
        for product_id in product_ids:
            for with_id in product_ids:
                # get the other products bought with each product
                if product_id != with_id:
                    # increment score for product purchased together
                    r.zincrby(self.get_product_key(product_id), 1, with_id)

    def suggest_products_for(
        self, products: list[Product], max_results: int = 6
    ) -> list[Product]:
        product_ids = [p.id for p in products]
        if len(products) == 1:
            suggestions = cast(
                list[Any],
                r.zrange(
                    self.get_product_key(product_ids[0]),
                    0,
                    max_results - 1,
                    desc=True,
                ),
            )
        else:
            # generate a temporary key
            flat_ids = "".join(str(product_id) for product_id in product_ids)
            tmp_key = f"tmp_{flat_ids}"
            # multiple products, combine scores of all products
            # store the resulting sorted set in a temporary key
            keys = [self.get_product_key(product_id) for product_id in product_ids]
            r.zunionstore(tmp_key, keys)
            # remove ids for the products the recommendation is for
            r.zrem(tmp_key, *product_ids)
            suggestions = cast(
                list[Any], r.zrange(tmp_key, 0, max_results - 1, desc=True)
            )
            # remove the temporary key
            r.delete(tmp_key)

        suggested_products_ids = [int(product_id) for product_id in suggestions]

        # get suggested products and sort by order of appearance
        suggested_products = list(Product.objects.filter(id__in=suggested_products_ids))
        suggested_products.sort(
            key=lambda product: suggested_products_ids.index(product.id)
        )
        return suggested_products

    def clear_purchases(self) -> None:
        for product_id in Product.objects.values_list("id", flat=True):
            r.delete(self.get_product_key(product_id))
