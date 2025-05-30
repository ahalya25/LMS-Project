from django.shortcuts import render

from django.views import View

from .models import Payment

from courses.models import Courses

from students.models import Students

# Create your views here.
class EntrollConfirmationView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid = uuid)

        payment,created = Payment.objects.get_or_create(student=Students.objects.get(profile=request.user),course=course,
                                      amount=course.offer_fee if course.offer_fee else course.fee)

        data = { 'payment' : payment }

        return render(request,'payments/enroll-confirmation.html',context=data)