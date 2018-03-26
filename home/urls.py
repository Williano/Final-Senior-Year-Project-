from django.conf.urls import url
from django.utils.translation import gettext_lazy as _
from . import views

urlpatterns = [
    url(
        regex=_(r'^$'),
        view=views.home,
        name='home'
    ),
 ]
