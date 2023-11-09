from django.shortcuts import render
from . import models
from django.contrib.gis.geos import Point
from django.http import JsonResponse
# Create your views here.
def update_location(request):
    try:
        print (request.POST.get('point',''))
        user_profle = models.Profile.objects.get(user=request.user)
        if not user_profle:
            raise ValueError("Can't get User details")
        point = request.POST["point"].split(",")
        point = [float(part) for part in point]
        point = Point(point, srid=4326)
        print(point)
        user_profle.location = point
        user_profle.save()
        return JsonResponse({"message": f"Set location to {point.wkt}."}, status=200)
    except Exception as e:
        raise e;
        #r