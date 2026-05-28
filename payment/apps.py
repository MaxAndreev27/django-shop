from django.apps import AppConfig
from django.conf import settings


class PaymentConfig(AppConfig):
    name = "payment"

    def ready(self):
        # stripe_live_mode = getattr(settings, "STRIPE_LIVE_MODE", "")
        # print(f"Live Mode {stripe_live_mode}")

        # Безпечно дістаємо ключ з налаштувань
        stripe_secret = getattr(settings, "STRIPE_SECRET_KEY", "") or ""

        if stripe_secret.startswith("sk_test_"):
            print("🚀 Stripe is in TEST mode for orders. Everything is safe.")
        elif stripe_secret.startswith("sk_live_"):
            print("🚨 ATTENTION: Stripe is connected to LIVE mode in the orders app!")
