from .models import GolfClub, GolfCourse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GolfClubForm, GolfCourseForm


def index(request):
    return render(request, 'golfcoursemap.html')


def golf_clubs_list(request):
    golf_clubs = GolfClub.objects.all()
    return render(request, 'allgolfclubs.html', {'golf_clubs': golf_clubs})

def add_golf_club(request):
    if request.method == 'POST':
        form = GolfClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('golf_clubs_list')  # Redirect to the list of golf clubs after adding
    else:
        form = GolfClubForm()

    return render(request, 'add_golf_club.html', {'form': form})


def golf_club_courses(request, golf_club_id):
    golf_club = get_object_or_404(GolfClub, pk=golf_club_id)
    courses = GolfCourse.objects.filter(golf_club=golf_club)
    return render(request, 'golf_club_courses.html', {'golf_club': golf_club, 'courses': courses})


def add_golf_course(request):
    if request.method == 'POST':
        form = GolfCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('golf_clubs_list')  # Redirect to the list of golf clubs after adding
    else:
        form = GolfCourseForm()

    return render(request, 'add_golf_course.html', {'form': form})

