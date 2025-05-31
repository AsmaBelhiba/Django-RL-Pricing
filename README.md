

```markdown
# 🛒 Dynamic Pricing API with Reinforcement Learning

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green?logo=django)](https://www.djangoproject.com/)
[![Stable Baselines3](https://img.shields.io/badge/Stable--Baselines3-RL-blueviolet)](https://stable-baselines3.readthedocs.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

This project is a Django-based API for e-commerce dynamic pricing, powered by **Reinforcement Learning** (OpenAI Gym + Stable Baselines3).  
Each product learns how to adjust its price based on stock levels, sales, and historical data — **automatically**.  
This project was proposed by Mr. [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi), a computer science teacher at the High Institute of Management of Tunis.

---

## 🚀 Features

- Django backend with **GraphQL** and **REST API** for product management
- **Custom OpenAI Gym environment** for pricing simulation
- **DQN Agent** using Stable-Baselines3 for intelligent price optimization
- OAuth2-based **token authentication** and **Postman-ready** testing
- **Rate limiting (throttling)** for pricing endpoints
- **Model training & prediction via Celery** background tasks
- Train, save, and load models per product
- CLI commands for price updates & model retraining
- Color-enhanced admin UI with price history logs
- Pipenv environment management

---

## 🛠️ Built With

- [Python 3.11](https://www.python.org/)
- [Django 4.x](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/)
- [OAuth2 Toolkit](https://django-oauth-toolkit.readthedocs.io/)
- [OpenAI Gym](https://www.gymlibrary.dev/)
- [Stable-Baselines3](https://stable-baselines3.readthedocs.io/)
- [Redis + Celery](https://docs.celeryq.dev/en/stable/)
- [Colorfield for Admin UI](https://pypi.org/project/django-colorfield/)

---

## ⚙️ Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/YOUR_USERNAME/dynamic_pricing_api.git
    cd dynamic_pricing_api
    ```

2. Install dependencies:

    ```bash
    pipenv install
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser (optional but recommended):

    ```bash
    python manage.py createsuperuser
    ```

5. Run the server:

    ```bash
    python manage.py runserver
    ```

6. **Start Redis (required for Celery):**

> ⚠️ You need to start **Redis** to use Celery.  
> I used **WSL (Windows Subsystem for Linux)** to launch Redis on Windows.  
> Example command inside WSL (Ubuntu):
> ```bash
> sudo service redis-server start
> ```

7. Start Celery workers and beat scheduler:

    ```bash
    celery -A pricing_api worker --loglevel=info --pool=solo
    celery -A pricing_api beat --loglevel=info
    ```

---

## 🔐 Authentication

The API uses **OAuth2 token-based authentication**:

1. Obtain a token:
    ```
    POST /o/token/ 
    with grant_type, client_id, client_secret, scope
    ```

2. Use the token in Postman under **Authorization → Bearer Token**

---

## 📮 REST API Endpoints

Examples:

```http
GET     /rest/products/
GET     /rest/products/categories/
POST    /rest/products/update-price/
```

🔐 Authentication & Security
Development Mode (DEBUG=True):
Authentication is disabled (AllowAny), so you can access the endpoints freely during local development.

---

## 🚦 Rate Limiting (Throttles)

To protect pricing endpoints, throttle rules are defined using DRF settings:

```python
'DEFAULT_THROTTLE_CLASSES': [
    'rest_framework.throttling.UserRateThrottle',
],
'DEFAULT_THROTTLE_RATES': {
    'user': '10/min',
}
```

---

## 📈 Usage

- Update all product prices via CLI:

    ```bash
    python manage.py update_product_prices
    ```

- Retrain RL models:

    ```bash
    python manage.py retrain_rl_models --timesteps 5000
    ```

---

## 🧩 GraphQL Examples

🔍 **List all products**:

```graphql
query {
  allProducts {
    id
    name
    currentPrice
    minPrice
    maxPrice
    stockQuantity
  }
}
```

🔁 **Update price for product with ID 6**:

```graphql
mutation {
  updatePrice(productId: 6, trainNew: true, timesteps: 5000) {
    success
    message
    priceChangePercent
  }
}
```

🧠 **Retrain all RL models**:

```graphql
mutation {
  retrainRlModels {
    success
    message
  }
}
```

GraphQL endpoint: `http://localhost:8000/graphql/`

---

## 📂 Project Structure

```
dynamic_pricing_api/
├── products/           # Product models, admin, serializers, GraphQL
├── rl_pricing/         # RL trainer, custom Gym env
├── pricing_api/        # Main Django config, URLs, settings
├── manage.py
├── Pipfile / Pipfile.lock
├── README.md
└── requirements.txt
```

---

## 🛣️ Roadmap

- ✅ DQN Agent integration
- ⏳ PPO, A2C agent support
- 🔁 Async parallel training
- 🧠 Reward shaping enhancements
- 📊 Admin dashboard for training analytics

---

## 🙌 Acknowledgements

- [Django](https://www.djangoproject.com)
- [Django REST Framework](https://www.django-rest-framework.org)
- [Stable-Baselines3](https://stable-baselines3.readthedocs.io/)
- [OpenAI Gym](https://www.gymlibrary.dev)
- [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/)
- [Redis & Celery](https://docs.celeryq.dev/en/stable/)
- [OAuth Toolkit](https://django-oauth-toolkit.readthedocs.io/)

---

Made with ❤️ by **Asma Belhiba** and **Rayane Kahlaoui**
```



