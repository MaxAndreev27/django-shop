# Multilingual E-Commerce Platform

A Django 6 e-commerce application with a localized product catalog, session-based cart, checkout, Stripe payments, background order processing, PDF invoices, and product recommendations. The interface and content support English and Ukrainian.

## Key Features

- **Product Catalog:** A dynamic product catalog with category filtering and localized content.
- **Shopping Cart:** A robust, session-based shopping cart allowing users to add, update, and remove products smoothly without forcing mandatory registration.
- **Custom Context Processors:** Tailored context processors to ensure application-wide availability of crucial data (such as the current cart state).
- **Order Management:** Full customer checkout workflows, order persistence, and order status tracking.
- **Asynchronous Task Queue:** Powered by **Celery** and **Redis** to offload heavy operations from the main request-response cycle.
- **Async Notifications:** Automatic email notifications sent asynchronously to customers upon successful order creation.
- **Background Task Monitoring:** Real-time visualization and management of Celery workers and tasks using **Flower**.
- **Secure Payment Processing:** Seamless checkout experience integrated with **Stripe** for processing credit card transactions securely.
- **Internationalization (i18n):** Full multilingual support (English & Ukrainian) for both static templates and dynamic database content via **django-parler**.
- **Invoicing & PDFs:** Automated generation of PDF invoices sent directly to customers or accessible via the admin panel.
- **Recommendation Engine:** A smart product recommendation mechanism suggesting items based on user purchase history ("People who bought this also bought...").

## Tech Stack

- **Framework:** Django 6.x
- **Database Multilingual Support:** django-parler
- **Task Queue:** Celery
- **Message Broker & Cache:** Redis
- **Monitoring Tool:** Flower
- **Payment Gateway:** Stripe API
- **Styling:** CSS3 & HTML5 (Fully Responsive/Mobile-friendly setup)

## Local Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/MaxAndreev27/django-shop.git
   cd django-shop
   ```

2. Create and activate a virtual environment, then install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. Start Redis in a separate terminal. For example, with Docker:

   ```bash
   docker run --rm -p 6379:6379 redis:latest
   ```

4. Configure environment variables for local development:

   ```bash
   export DJANGO_SECRET_KEY="replace-with-a-local-secret"
   export DEBUG=True
   export REDIS_URL="redis://127.0.0.1:6379/0"
   export STRIPE_PUBLISHABLE_KEY="pk_test_..."
   export STRIPE_SECRET_KEY="sk_test_..."
   export STRIPE_WEBHOOK_SECRET="whsec_..."
   ```

5. Prepare the database and start the development server:

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

6. In another terminal, run the background worker when you need asynchronous order notifications:
   ```bash
   celery -A config worker --loglevel=info
   ```

The site is available at `http://127.0.0.1:8000/`. Flower can be started with `celery -A config flower --port=5555`.

## Tests

Run the Django test suite with:

```bash
python manage.py test
```

## Deployment

The repository includes a Dockerfile and a GitHub Actions workflow for deployment to Fly.io. Configure `FLY_API_TOKEN` as an Actions secret before deploying from the `main` branch.

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Security

For responsible disclosure instructions, see [SECURITY.md](SECURITY.md).

## License

This project is distributed under the [MIT License](LICENSE).
