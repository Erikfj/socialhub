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
    hubs = Hub.objects.all()
    context = {'hubs': hubs}
    return render(request, 'hubs/hub_listing.html', context)


def hub_details(request, hub_id):
    hub = Hub.objects.get(pk=hub_id)

    if request.method == "POST":
        new_note_text = request.POST.get('new_note')
        new_note = HubNote()
        new_note.note = new_note_text
        new_note.hub = hub
        new_note.created_by = request.user
        new_note.created_datetime = timezone.now()
        new_note.save()

    # notes = hub.notes.all() Det kom en feil her da hub ikke har noe attributt notes. men note
    notes = HubNote.objects.all()
    page_number = request.GET.get('page')
    pageinator = Paginator(notes, 5)
    try:
        notes = pageinator.page(page_number)
    except PageNotAnInteger:
        notes = pageinator.page(1)
    except EmptyPage:
        notes = pageinator.page(pageinator.num_pages)

    context = {
        'hub': hub,
        'notes': notes}
    return render(request, 'hubs/hub_details.html', context)


@csrf_exempt
def student_note_add_points(request, student_id, note_id):
    note = StudentNote.objects.get(pk=note_id)
    note.points = note.points + 1
    note.save()
    data = {'points_updated': note.points}
    return JsonResponse(data)
