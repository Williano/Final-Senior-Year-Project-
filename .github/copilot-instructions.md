# E-Shopper Django E-Commerce Platform - AI Agent Guide

This is a multi-lingual Django e-commerce platform with 10 international language support, PayPal integration, and Redis-based recommendations.

## Core Architecture

### Multi-language Strategy
- Uses `django-parler` for model translations, not Django's standard i18n
- Models like `Product` and `Category` have `TranslatableModel` with `TranslatedFields`
- URLs wrapped in `i18n_patterns()` with language-specific routing
- Template translations use `{% load i18n %}` and `{% trans "text" %}`
- Language configuration in `PARLER_LANGUAGES` setting (10 languages supported)

### Key Components & Data Flow
- **Cart System**: Session-based cart (`cart/cart.py`) with context processor for global template access
- **Orders**: Order creation triggers Celery email tasks (`orders/tasks.py`)
- **Payments**: PayPal IPN integration (`payment/views.py`) with order completion workflow
- **Recommendations**: Redis-based product recommendations (`onlineshop/recommender.py`)
- **Search**: Django-Watson for full-text search across products
- **Admin**: django-jet with Google Analytics dashboard integration

### Database & External Services
- **MySQL 8** as primary database (see `DATABASES` in settings)
- **Redis** for cart sessions, recommendations, and Celery broker
- **Celery** for async tasks (email notifications, background processing)
- **SendGrid** for email backend
- **PayPal** for payment processing (test mode configured)

## Development Workflows

### Essential Commands
```bash
# Database setup (MySQL required)
python manage.py migrate
python manage.py createsuperuser

# Start Redis (required for recommendations/sessions)
redis-server

# Start Celery worker (for email tasks)
celery -A eshopper worker -l info

# Run development server
python manage.py runserver
```

### Key Environment Requirements
- MySQL 8 server running with database 'eshopper'
- Redis server for sessions and recommendations
- Python 3 with mysqlclient package (requires MySQL dev headers on Linux)

## Project-Specific Patterns

### Model Translations
When adding translatable content:
```python
class MyModel(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, db_index=True),
        slug=models.SlugField(max_length=200, db_index=True, unique=True)
    )
    # Non-translatable fields go outside
    price = models.DecimalField(max_digits=10, decimal_places=2)
```

### Cart Integration
- Cart object available in all templates via context processor
- Session key: `settings.CART_SESSION_ID` ('cart')
- Cart methods: `add()`, `remove()`, `clear()`, `get_total_price()`

### Order Processing Flow
1. Cart → Checkout form → Order creation
2. Order triggers Celery task for confirmation email
3. PayPal payment → IPN webhook → Order marked as paid
4. Product recommendations updated via Redis

### Admin Customization
- Uses django-jet with custom dashboard (`dashboard.py`)
- Google Analytics integration configured
- Import/export functionality for products

## Critical Integration Points

### URL Patterns
- All user-facing URLs wrapped in `i18n_patterns()`
- Admin URLs use jet dashboard extensions
- PayPal IPN endpoints for payment webhooks

### Settings Dependencies
- `CART_SESSION_ID` for cart functionality
- `PAYPAL_RECEIVER_EMAIL` and `PAYPAL_TEST` for payments
- `REDIS_HOST/PORT/DB` for recommendations and sessions
- `PARLER_LANGUAGES` for translation configuration

### Template Structure
- Base template: `onlineshop/base.html`
- Each app has its own `templates/` directory
- Translation strings use `{% trans %}` tags throughout

## Testing & Debugging
- Products, orders, and cart functionality depend on MySQL being properly set up
- Email functionality requires Celery worker running
- Payment testing uses PayPal sandbox mode
- Recommendations require Redis for proper functionality

When modifying this codebase, always consider the multi-language implications and ensure both translated and non-translated fields are handled appropriately.