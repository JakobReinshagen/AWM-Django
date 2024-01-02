from .models import GolfClub, GolfCourse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GolfClubForm, GolfCourseForm


def index(request):
    return render(request, 'golfcoursemap.html')


def golf_clubs_list(request):
    golf_clubs = GolfClub.objects.all()
    return render(request, 'allgolfclubs.html', {'golf_clubs': golf_clubs})


def add_golf_course(request, golf_club_id):
    if request.method == 'POST':
        golf_clubIN = get_object_or_404(GolfClub, pk=golf_club_id)
        golfCourse = GolfCourse(name=request.POST["name"], golf_club=golf_clubIN, calculated_distance=request.POST["distance"], estimated_hits=["hits"], point1long=["point1long"], points1lat=["point1lat"], point2long=["point2long"], points2lat=["point2lat"], point3long=["point3long"], points3lat=["point3lat"])
        golfCourse.save()
        return redirect('golf_clubs_list')  # Redirect to the list of golf clubs after adding
    else:
        form = GolfCourseForm()
    golf_club = get_object_or_404(GolfClub, pk=golf_club_id)

    return render(request, 'add_golf_course.html', {'golf_club': golf_club})

def add_golf_courseData(request):
    if request.method == 'POST':
        golf_clubIN = get_object_or_404(GolfClub, pk=request.POST["club_id"])
        golfCourse = GolfCourse(name=request.POST["name"], golf_club=golf_clubIN, calculated_distance=request.POST["distance"], estimated_hits=request.POST["estimated_hits"], point1long=request.POST["point1long"], point1lat=request.POST["point1lat"], point2long=request.POST["point2long"], point2lat=request.POST["point2lat"], point3long=request.POST["point3long"], point3lat=request.POST["point3lat"])
        golfCourse.save()
        return redirect('golf_clubs_list')

def golf_club_courses(request, golf_club_id):
    golf_club = get_object_or_404(GolfClub, pk=golf_club_id)
    courses = GolfCourse.objects.filter(golf_club=golf_club)
    return render(request, 'golf_club_courses.html', {'golf_club': golf_club, 'courses': courses})


def add_golf_club(request):
    print("received data")
    try:
        if request.method == 'POST':
            golfclub = GolfClub(name=request.POST["name"], location_latitude=request.POST["location_latitude"], location_longitude=request.POST["location_longitude"])
            golfclub.save()
            return redirect('golf_clubs_list')  # Redirect to the list of golf clubs after adding
    except Exception as e:
        raise e



def add_golf_club(request):
    if request.method == 'POST':
        form = GolfClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('golf_clubs_list')  # Redirect to the list of golf clubs after adding
    else:
        form = GolfClubForm()

    return render(request, 'add_golf_club.html', {'form': form})


