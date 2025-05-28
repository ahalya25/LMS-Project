from django.shortcuts import render ,redirect

from django.views import View

from django.db import transaction

from lms.utility import send_email

from .forms import InstructorForm

from students.forms import ProfileForm

import threading

# Create your views here.
class InstructorRegisterView(View):

    def get(self,request,*args,**kwargs):

        profile_form = ProfileForm()

        instructor_form = InstructorForm()

        data = {'profile_form' : profile_form,'instructor_form':instructor_form}

        return render(request,'instructors/instructor-register.html',context=data)
    
    # def post(self, request, *args , **kwargs):

    #     profile_form = ProfileForm(request.POST)

    #     print(profile_form.errors)

    #    instructor_form = InstructorForm(request.POST, request.FILES)

    #     print(instructor_form.errors)



    #     if profile_form.is_valid():

    #         with transaction.atomic():

    #             profile = profile_form.save(commit=False)

    #             email = profile_form.cleaned_data.get('email')

    #             password = profile_form.cleaned_data.get('password')

    #             profile.username = email

    #             profile.role = 'Student'

    #             profile.password = make_password(password)

    #             profile.save()

    #             if instrucor_form.is_valid():

    #                 instructor = instructor_form.save(commit=False)

    #                 instructor.profile = profile

    #                 instructor.name = f'{profile.first_name} {profile.last_name}'

    #                 instructor.save()

    #                 subject = 'Successfully Registered'

    #                 recipient = student.profile.email

    #                 template = 'email/success-registertion.html'

    #                 context = {'name': student.name,'username':student.profile.email,'password':password }

    #                 thread = threading.Thread(target=send_email,args=(subject,recipient,template,context))

    #                 # send_email(subject,recipient,template,context)
    #                 thread.start()

    #                 return redirect('login')
            
    #     data = {'profile_form' : profile_form, 'student_form': student_form}

    #     return render(request,'students/student-register.html',context=data)