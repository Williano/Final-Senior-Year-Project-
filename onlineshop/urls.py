from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
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


