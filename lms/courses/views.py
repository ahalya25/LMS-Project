from django.shortcuts import render , redirect

from django.views import View

from .models import Courses,CategoryChoice,LevelChoices

from .forms import CoursesCreateForm

from instructors.models import Instructors

from django.db.models import Q

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_roles

from lms.utility import get_recommended_courses

# Create your views here.

class CoursesListView(View):

    def get(self,request,*args,**kwargs):

        # fetching all courses from courses model

        query = request.GET.get('query')

        # print(query)

        courses = Courses.objects.all()

        if query :

            courses = Courses.objects.filter(Q(title__icontains=query)|
                                             Q(description__icontains=query)|
                                             Q(instructor__name__icontains=query)|
                                             Q(category__icontains=query)|
                                             Q(type__icontains=query)|
                                             Q(level__icontains=query)|
                                             Q(fee__icontains=query))

       

        data = {'courses':courses, 'page':'courses-page' ,'query' : query }

        return render(request,'courses/courses-list.html',context=data)
    
    
class CoursesDetailView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid)

        recommended_courses = get_recommended_courses(course)

        data = {'course' : course }

        return render(request,'courses/course-detail.html',context=data)     
    

class HomeView(View):

    def get(self,request,*args,**kwargs):

        data ={'page': 'home-page'} 

        return render(request,'courses/home.html',context=data) 


# @login_required(login_url='login')     

# @method_decorator(login_required(login_url='login'),name='dispatch')

@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')
class InstructorcourseListView(View):

    def get(self,request,*args,**kwargs) :

        instructor = Instructors.objects.get(profile=request.user)
        # print(courses)
        query = request.GET.get('query')

        courses = Courses.objects.filter(instructor=instructor)

        if query :

            courses = Courses.objects.filter(Q(title__icontains=query)|
                                             Q(description__icontains=query)|
                                             Q(instructor__name__icontains=query)|
                                             Q(category__icontains=query)|
                                             Q(type__icontains=query)|
                                             Q(level__icontains=query)|
                                             Q(fee__icontains=query))


        data ={'page' : 'instructor-courses-page','courses': courses , 'query': query}

        return render(request,'courses/instructor-courses-list.html',context=data)
    
    # Normal way
# @method_decorator(login_required(login_url='login'),name='dispatch') 
@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')  
class CourseCreateView(View):

    def get(self,request,*args,**kwargs):

        form = CoursesCreateForm()

        data = {'form' : form } 

        # data ={'categories': CategoryChoice,'levels':LevelChoices }    

        return render(request,'courses/course-create.html',context=data)
    
    def post(self,request,*args,**kwargs):


        # print(title,image,description,category,level,fee,offer_fee)

# with the help of django-forms        

        form = CoursesCreateForm(request.POST,request.FILES)

        instructor = Instructors.objects.get(id=1)

        if form.is_valid():

            # print(form.cleaned_data)

            # form.cleaned_data['instructor'] = 'Jhon Doe'

            # form.save()

            course = form.save(commit=False)

            # Course.instructor = 'Jhon Doe'

            course.instructor = instructor

            course.save()

            return redirect('instructor-courses-list')
        
        data = {'form' : form }
        
        return render(request,'courses/course-create.html',context=data)
    
# @method_decorator(login_required(login_url='login'),name='dispatch') 

@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')   
class InstructorCoursesDetailView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid)

        data = {'course' : course }

        return render(request,'courses/instructor-courses-detail.html',context=data) 
    
@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')
class InstructorCourseDeleteView(View):

    def get(self,request,*args,**kwargs):

        uuid =kwargs.get('uuid') #pick id

        course = Courses.objects.get(uuid=uuid) #orm 

        course.delete()

        return redirect('instructor-courses-list') 

# @method_decorator(login_required(login_url='login'),name='dispatch')

@method_decorator(permission_roles(roles=['Instructor']),name='dispatch')
class InstructorCourseUpdateView(View):

    def get(self,request,*args,**kwargs):

        id = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid)

        form = CoursesCreateForm(instance=course)

        data = {'form' : form }

        return render(request,'courses/instructor-course-update.html',context=data) 

    def post(self,request,*args,**kwargs) :

        id = kwargs.get('uuid')

        course = Courses.objects.get(uuid=uuid) 

        form = CoursesCreateForm(request.POST,request.FILES,instance=course)

        if form.is_valid(): # check for data is valid

            form.save()  

            return redirect('instructor-courses-list') 

        data = {'form' : form }

        return render(request,'courses/instructor-course-update.html',context = data)             
    



