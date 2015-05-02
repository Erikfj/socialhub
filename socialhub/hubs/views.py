from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone

from hubs.models import HubNote


# Create your views here.
def hub_listing(request):
    hubs = Hub.objects.all()
    context = {'hubs': hubs}
    return render(request, 'hubs/hub_listing.html', context)

def hub_details(request, hub_id):
	# this view renders hub details and all notes saved to the hub.
	hub = Hub.objects.get(pk=hub_id)