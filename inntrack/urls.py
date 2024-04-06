from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("", views.login, name="login"),
               path('', views.shipment, name='shipment'),
               path('index.html', views.index, name='index'),
               path('service.html', views.service, name='service'),
               path('about.html', views.about, name='about'),
               path('contact.html', views.contact, name='contact'),
               path('shipment', views.shipment, name='shipment'),]
