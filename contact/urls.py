from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        regex=r'^$',
        view=views.contact,
        name='contact'
    ),

    url(
        regex=r'^email_success/$',
        view=views.email_success,
        name='email_success'
    ),
 ]
