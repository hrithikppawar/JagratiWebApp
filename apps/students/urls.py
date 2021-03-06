from django.urls import path

from . import views

app_name = 'students'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_student, name='new_student'),
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('attendance/', views.attendance, name='attendance'),
    path('ajax/attendance/', views.ajax_attendance, name='ajax_attendance'),
    # path('attendance/view/', views.view_attendance, name='view_attendance'),
    path('profile/update/', views.update_profile, name='update_profile'),  # Not needed, update in profile/ only

    path('update_from_sheets/', views.update_from_sheets, name='update_from_sheets'),
]