from django.urls import path

from . import views

urlpatterns = [

    path('enroll-confirmation/<str:uuid>/',views.EntrollConfirmationView.as_view(),name='enroll-confirmation')
]