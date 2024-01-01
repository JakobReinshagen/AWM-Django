# urls.py
from django.urls import path
from .views import start_record, pause_record, resume_record, stop_record, trail_detail, get_trail_path

urlpatterns = [
    path('start/', start_record, name='start_record'),
    path('<int:trail_id>/pause/', pause_record, name='pause_record'),
    path('<int:trail_id>/resume/', resume_record, name='resume_record'),
    path('<int:trail_id>/stop/', stop_record, name='stop_record'),
    path('<int:trail_id>/', trail_detail, name='trail_detail'),
    path('api/trail/<int:trail_id>/path/', get_trail_path, name='get_trail_path'),
]
