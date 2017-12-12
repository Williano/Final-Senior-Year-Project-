from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        regex=r'^$',
        view=views.cart_detail,
        name='cart_detail'
    ),

    url(
        regex=r'^add/(?P<product_id>\d+)/$',
        view=views.cart_add,
        name='cart_add'
    ),

    url(
        regex=r'^remove/(?P<product_id>\d+)/$',
        view=views.cart_remove,
        name='cart_remove'
    ),

]
