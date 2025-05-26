from django.shortcuts import render , redirect

# Create your views here.
from django.views import View

from .forms import ProfileForm , StudentForm

from django.contrib.auth.hashers import make_password

class StudentRegisterView(View):

    def get(self,request,*args,**kwargs):

        profile_form = ProfileForm()

        student_form = StudentForm()

        data = {'profile_form' : profile_form,'student_form':student_form}

        return render(request,'students/student-register.html',context=data)
    
    def post(self, request, *args , **kwargs):

        profile_form = ProfileForm(request.POST)

        print(profile_form.errors)

        student_form = StudentForm(request.POST, request.FILES)

        print(student_form.errors)



        if profile_form.is_valid():

            profile = profile_form.save(commit=False)

            email = profile_form.cleaned_data.get('email')

            password = profile_form.cleaned_data.get('password')

            profile.username = email

            profile.role = 'Student'

            profile.password = make_password(password)

            profile.save()

            if student_form.is_valid():

                student = student_form.save(commit=False)

                student.profile = profile

                student.name = f'{profile.first_name} {profile.last_name}'

                

                student.save()

                return redirect('login')
            
        data = {'profile_form' : profile_form, 'student_form': student_form}

        return render(request,'students/student-register.html',context=data)