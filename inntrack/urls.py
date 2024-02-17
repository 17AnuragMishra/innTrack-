from django.urls import path

from . import views

urlpatterns = [path("", views.index, name="index"),
               path("", views.login, name="login"),
               path('service.html', views.service, name='service'),
               path('about.html', views.about, name='about'),
               path('contact.html', views.contact, name='contact'),
               path('shipment_details.html', views.shipment, name='shipment')]

#from .views import get_shipment_details

#urlpatterns = [
#    path('get_shipment_details/', get_shipment_details, name='get_shipment_details'),
#    # Add other URL patterns as needed
#]