from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ide/', views.ide, name='ide'),
    path('courses/', views.courses, name='courses'),
    path('courses/<str:course_name>', views.course, name='course'),
]
