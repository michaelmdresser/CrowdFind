from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^register/$', views.register, name="index"),
    url(r'^$', views.login, name="login")
   # url(r'^register/$', views.register, name='register')
]