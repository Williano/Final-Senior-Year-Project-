"""eshopper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from jet.dashboard.dashboard_modules import google_analytics_views


urlpatterns = i18n_patterns(
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^profile/', include('registration.urls', namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('home.urls', namespace='home')),
    url(_(r'^faq/'), include('faq.urls', namespace='faq')),
    url(_(r'^privacy/'), include('privacy-policy.urls', namespace='privacy')),
    url(_(r'^refund/'), include('refund-policy.urls', namespace='refund')),
    url(_(r'^about/'), include('about.urls', namespace='about')),
    url(_(r'^contact/'), include('contact.urls', namespace='contact')),
    url(_(r'coupons/'), include('coupons.urls', namespace='coupons')),
    url(_(r'^orders/'), include('orders.urls', namespace='orders')),
    url(_(r'^cart/'), include('cart.urls', namespace='cart')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
    url(_(r'^payment/'), include('payment.urls', namespace='payment')),
    url(r"^search/", include("watson.urls", namespace="watson")),
    url(_(r'^onlineshop/'), include('onlineshop.urls', namespace='onlineshop')),
)

if settings.DEBUG:
            urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)