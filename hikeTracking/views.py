from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from .models import Trail

@login_required
def start_record(request):
    # Create a new trail record when the user starts recording
    new_trail = Trail.objects.create(user=request.user, started_at=timezone.now(), name="New Trail")
    request.session['trail_id'] = new_trail.id
    return redirect('trail_detail', trail_id=new_trail.id)

@login_required
def pause_record(request, trail_id):
    # Pause the recording by updating the ended_at field
    trail = Trail.objects.get(id=trail_id)
    trail.ended_at = timezone.now()
    trail.save()
    return redirect('trail_detail', trail_id=trail_id)

@login_required
def resume_record(request, trail_id):
    # Resume the recording by setting ended_at to None
    trail = Trail.objects.get(id=trail_id)
    trail.ended_at = None
    trail.save()
    return redirect('trail_detail', trail_id=trail_id)

@login_required
def stop_record(request, trail_id):
    # Stop the recording and finalize the trail
    trail = Trail.objects.get(id=trail_id)
    trail.ended_at = timezone.now()
    trail.save()
    return redirect('trail_detail', trail_id=trail_id)

@login_required
def trail_detail(request, trail_id):
    # Get the current trail and display its details
    trail = Trail.objects.get(id=trail_id)
    return render(request, 'trail_detail.html', {'trail': trail})

@login_required
def get_trail_path(self, request, trail_id):
    try:
        trail = Trail.objects.get(pk=trail_id)
        # Assuming your Trail model has a GeoJSON field named 'path'
        trail_path_geojson = trail.path.geojson
        return JsonResponse(trail_path_geojson)
    except Trail.DoesNotExist:
        return JsonResponse({'error': 'Trail not found'}, status=404)



