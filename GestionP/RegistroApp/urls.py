
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_view, name='RegistroApp.index'),
    url(r'^login/$', views.login_view, name='RegistroApp.login'),
]