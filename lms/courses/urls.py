from django.urls import path

from . import views

urlpatterns=[

    
    path('course-detail/<str:uuid>/',views.CoursesDetailView.as_view(),name='course-detail'),

    path('home/',views.HomeView.as_view(),name='home'),

    path('instructor-courses-list/',views.InstructorcourseListView.as_view(),name='instructor-courses-list'),

    path('create-course/',views.CourseCreateView.as_view(),name='create-course'),

    path('instructor-courses-detail/<str:uuid>/',views.InstructorCoursesDetailView.as_view(),name='instructor-courses-detail'),

    path('instructor-courses-delete/<str:uuid>/',views.InstructorCourseDeleteView.as_view(),name='instructor-courses-delete'),

    path('instructor-courses-update/<str:uuid>/',views.InstructorCourseUpdateView.as_view(),name='instructor-courses-update'),

   
]
