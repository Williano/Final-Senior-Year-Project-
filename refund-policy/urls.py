from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.refund,
        name='refund-policy'
    ),
 ]
