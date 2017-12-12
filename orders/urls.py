from django.conf.urls import url
from . import views


urlpatterns = [

    url(
        regex=r'^create/$',
        view=views.order_create,
        name='order_create'
    ),
]