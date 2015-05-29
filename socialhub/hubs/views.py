from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from hubs.models import Hub
from hubs.models import HubNote


# Create your views here.
def hub_listing(request):

    if request.method == "POST":
        new_topic_text = request.POST.get('new_topic')
        new_topic = Hub()
        new_topic.topic = new_topic_text
        new_topic.created_by = request.user
        new_topic.created_datetime = timezone.now()
        new_topic.username = request.user

        new_topic.save()

    hubs = Hub.objects.all()
    for hub in hubs: 
    	print hub
    context = {'hubs': hubs}
    return render(request, 'hubs/hub_listing.html', context)


def hub_details(request, hub_id):
    hub = Hub.objects.get(pk=hub_id)

    # notes = hub.topics.all() Det kom en feil her da hub ikke har noe attributt notes. men note
    topics = Hub.objects.all()
    page_number = request.GET.get('page')
    pageinator = Paginator(topics, 5)
    try:
        topics = pageinator.page(page_number)
    except PageNotAnInteger:
        topics = pageinator.page(1)
    except EmptyPage:
        topics = pageinator.page(pageinator.num_pages)

    context = {
        'hub': hub,
        'topics': topics}
    return render(request, 'hubs/hub_details.html', context)


@csrf_exempt
def hub_topic_add_points(request, username_id, topic_id):
    topic = Hub.objects.get(pk=topic_id)
    topic.hubpoints = topic.hubpoints + 1
    topic.save()
    data = {'points_updated': topic.hubpoints}
    return JsonResponse(data)
