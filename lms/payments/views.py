from django.shortcuts import render

from django.views import View

from .models import Payment

from courses.models import Courses

from students.models import Students

from .models import Transactions

import razorpay

from decouple import config

# Create your views here.
class EntrollConfirmationView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid = uuid)

        payment,created = Payment.objects.get_or_create(student=Students.objects.get(profile=request.user),course=course,
                                      amount=course.offer_fee if course.offer_fee else course.fee)

        data = { 'payment' : payment }

        return render(request,'payments/enroll-confirmation.html',context=data)

class RazorpayView(View):


    def get(self, request, *args, **kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid)

        payment = Payment.objects.get(student__profile = request.user, course=course)

        transaction = Transactions.objects.create(payment=payment)

        client = razorpay.Client(auth=(config("RZP_CLIENT_ID"), config("RZP_CLIENT_SECRET")))

        data = { "amount": payment.amount*100, "currency": "INR", "receipt": "order_rcptid_11" }
        
        order = client.order.create(data=data)  

        # print(order)

        rzp_order_id = order.get('id')

        transaction.rzp_order_id = rzp_order_id

        transaction.save()

        data = {'client_id' : config("RZP_CLIENT_ID"), 'rzp_order_id' : rzp_order_id ,'amount' : payment.amount*100}

        return render(request,'payments/payment-page.html',context=data)        