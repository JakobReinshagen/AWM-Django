from django.db import models


class GolfClub(models.Model):
    name = models.CharField(max_length=255)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()

    def __str__(self):
        return self.name


class GolfCourse(models.Model):
    name = models.CharField(max_length=255)
    golf_club = models.ForeignKey(GolfClub, on_delete=models.CASCADE)
    calculated_distance = models.FloatField()
    estimated_hits = models.IntegerField()
    point1lat = models.FloatField()
    point1long = models.FloatField()
    point2lat = models.FloatField()
    point2long = models.FloatField()
    point3lat = models.FloatField()
    point3long = models.FloatField()
    points = models.JSONField()

    def __str__(self):
        return self.name

