from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('code_editor/', views.ide, name='code_editor'),
    path('open_challenge/<str:course_name>/<str:section>/', views.open_challenge, name='open_challenge'),
    path('check_challenge/<str:course_name>/<str:section>/<str:output>/', views.check_challenge, name='check_challenge'),
    path('courses/', views.courses, name='courses'),
    path('courses/<str:course_name>/', views.course, name='course'),
    path("update-note-order/", views.update_note_order, name="update_note_order"),
    path("delete-note/<int:note_id>/", views.delete_note, name="delete_note"),
]
