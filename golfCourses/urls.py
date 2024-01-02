from django.urls import path
from .views import index, golf_clubs_list, add_golf_club, add_golf_course, add_golf_club, golf_club_courses

urlpatterns = [
    path('', index, name='index'),
    path('allgolfclubs/', golf_clubs_list, name='golf_clubs_list'),
    path('add-golf-club/', add_golf_club, name='add_golf_club'),
    path('golf-club-courses/<int:golf_club_id>/', golf_club_courses, name='golf_club_courses'),
    path('add-golf-course/<int:golf_club_id>/', add_golf_course, name='add_golf_course'),
]