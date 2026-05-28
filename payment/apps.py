from django.apps import AppConfig
from django.conf import settings


class PaymentConfig(AppConfig):
    name = "payment"

    def ready(self):
        # Оператор `or ""` гарантує: якщо там None, ми отримаємо порожній рядок ""
        stripe_secret = getattr(settings, "STRIPE_SECRET_KEY", "") or ""

        if stripe_secret.startswith("sk_test_"):
            print("🚀 Stripe is in TEST mode for orders. Everything is safe.")
        elif stripe_secret.startswith("sk_live_"):
            print("🚨 ATTENTION: Stripe is connected to LIVE mode in the orders app!")
        else:
            # Цей блок спрацює під час деплою на Fly.io, коли секрети приховані
            print("⚠️ Stripe key is empty. (Normal behavior during Docker build)")
