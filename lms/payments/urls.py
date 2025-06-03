from django.urls import path

from . import views

urlpatterns = [

    path('enroll-confirmation/<str:uuid>/',views.EntrollConfirmationView.as_view(),name='enroll-confirmation'),
    path('razorpay-view/<str:uuid>', views.RazorpayView.as_view(),name= 'razorpay-view'),
    path('verify-payment/',views.PaymentverifyView.as_view(),name='verify-payment')
]
