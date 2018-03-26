from django.conf.urls import url
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = [
    url(
        regex=_(r'^product_list/$'),
        view=views.product_list,
        name='product_list'
    ),

    url(
        regex=r'^(?P<category_slug>[-\w]+)/$',
        view=views.product_list,
        name='product_list_by_category'
    ),

    url(
        regex=r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        view=views.product_detail,
        name='product_detail'),

]


