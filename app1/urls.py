from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('course-grid-2/', views.course_grid_2, name='course_grid_2'),
    path('course-grid-3/', views.course_grid_3, name='course_grid_3'),
    path('course-grid-4/', views.course_grid_4, name='course_grid_4'),
    path('teacher_home/', views.sign_in, name='teacher_home'),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers_official/', views.teachers_official, name='teachers_official'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('profile_update', views.profile_update, name='profile_update'),
    path('assignment_save', views.assignment_save, name='assignment_save'),
    path('materials_save', views.materials_save, name='materials_save'),
    path('class_save', views.class_save, name='class_save'),
    path('qp_save', views.qp_save, name='qp_save'),
    path('photo_save', views.photo_save, name='photo_save'),
]