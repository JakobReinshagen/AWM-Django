# In views.py

from django.http import JsonResponse
from django.views import View
from .models import Trail

class TrailPathAPIView(View):
    def get(self, request, trail_id):
        try:
            trail = Trail.objects.get(pk=trail_id)
            # Assuming your Trail model has a GeoJSON field named 'path'
            trail_path_geojson = trail.path.geojson
            return JsonResponse(trail_path_geojson)
        except Trail.DoesNotExist:
            return JsonResponse({'error': 'Trail not found'}, status=404)
