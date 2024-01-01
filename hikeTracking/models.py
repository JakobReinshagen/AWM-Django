from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Trail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    path = models.LineStringField(srid=4326)
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        app_label = 'hikeTracking'
