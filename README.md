# Multilingual E-Commerce Platform (Django 6)

A fully featured, production-ready e-commerce platform built with **Django 6**. This project implements advanced web development practices, including session-based shopping carts, asynchronous task processing, secure payment integration, and complete internationalization.

## 🚀 Key Features

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

## 🛠️ Tech Stack

- **Framework:** Django 6.x
- **Database Multilingual Support:** django-parler
- **Task Queue:** Celery
- **Message Broker & Cache:** Redis
- **Monitoring Tool:** Flower
- **Payment Gateway:** Stripe API
- **Styling:** CSS3 & HTML5 (Fully Responsive/Mobile-friendly setup)

## 🔧 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/MaxAndreev27/django-shop.git](https://github.com/MaxAndreev27/django-shop.git)
   cd django-shop
   ```
