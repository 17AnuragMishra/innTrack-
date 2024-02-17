from django.shortcuts import render#, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def contact(request):
    return render(request, 'contact.html')
    
def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def shipment(request):
    return render(request, 'shipment_details.html')












































#from .models import Shipment
# views.py
'''def get_shipment_details(request, order_number):
    try:
        shipment = Shipment.objects.get(order_number=order_number)
        # Access other shipment details using shipment.<field_name>
        return render(request, 'index.html', {'shipment': shipment})
    except Shipment.DoesNotExist:
        return render(request, 'shipment_not_found.html', {'order_number': order_number})

# views.py or any other Django file where you want to insert data

from .models import Shipment

# Create instances of the Shipment model
shipment1 = Shipment(member_id='Flipkart', order_number='123456' , tracking_id='1864575IT', priority='4', current_location='lucknow', destination='cantt lucknow', delivery_date='2024-02-10')
shipment2 = Shipment(member_id='Ebay', order_number='4489911', tracking_id='1648526IT', priority='4', current_location='lucknow', destination='cantt lucknow', delivery_date='2024-02-10')
shipment3 = Shipment(member_id='Amazon', order_number='8419859', tracking_id='1622366IT', priority='4', current_location='lucknow', destination='cantt lucknow', delivery_date='2024-02-10')

# Save the instances to the database
shipment1.save()
shipment2.save()
shipment3.save()

# views.py

from .models import Shipment

def get_shipment_details(request):
    if request.method == 'GET':
        order_number = request.GET.get('order_number')
        shipment = get_object_or_404(Shipment, order_number=order_number)
        return render(request, 'shipment_details.html', {'shipment': shipment})
    return render(request, 'shipment_form.html')
'''