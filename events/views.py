from django.shortcuts import render, redirect,\
                        reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Event
from .forms import EventForm


def events(request):
    """
    A view to return a page with listed events
    """
    events = Event.objects.all()

    context = {
        'events': events,  
    }    
    return render(request, 'events/events.html', context)


def event(request, event_id):
    """
    A view of one event
    """
    events = Event.objects.all()
    event = get_object_or_404(events, pk=event_id)

    context = {
        'event': event,   
    }    
    return render(request, 'events/event.html', context)


@login_required
def add_event(request):
    """ Add an event """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            events = form.save()
            messages.success(request, 'Successfully added event.')
            return redirect('events')
            #return redirect(reverse('event', args=[event.id]))
        else:
            messages.error(request, 'Failed to add event. Please check if the form is valid.')
    else:
        form = EventForm()    
    
    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """ Edit an event  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('event', args=[event.id]))
        else:
            messages.error(request, 'Failed to update event. Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title} on {event.date}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """ Delete an event  """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.info(request, 'Event deleted!')
    
    return redirect(reverse('events'))
