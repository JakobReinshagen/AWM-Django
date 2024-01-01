from django import forms
from .models import GolfClub
from .models import GolfCourse


class GolfClubForm(forms.ModelForm):
    class Meta:
        model = GolfClub
        fields = ['name', 'location_latitude', 'location_longitude']


class GolfCourseForm(forms.ModelForm):
    class Meta:
        model = GolfCourse
        fields = ['name', 'golf_club', 'calculated_distance', 'estimated_hits', 'points']

