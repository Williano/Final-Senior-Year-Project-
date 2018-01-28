from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^apply/$',
        view=views.coupon_apply,
        name='apply'
    ),
]
