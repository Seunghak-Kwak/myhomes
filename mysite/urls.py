from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^success/', views.submit_ok, name='submit_ok'),
    url(r'^index/', views.index, name='index' ),
    url(r'^old/', views.data_list, name='data_list'),
]