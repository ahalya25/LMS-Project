from django.db import models

import uuid

# from instructors.models import Instructors

# Create your models here.

# category_choice = [

#     ('IT & software','IT & software'),
#     ('Finance','Finance'),
#     ('Marketing','Marketing')
# ]

class BaseClass(models.Model):

    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at =  models.DateTimeField(auto_now_add=True)

    updated_at =  models.DateTimeField(auto_now=True)

    class Meta: # set for abstract class

        abstract = True


class CategoryChoice(models.TextChoices):

    IT_SOFTWARE = 'IT & software','IT & software'

    FINANCE = 'finace','finance'

    MARKETING ='Marketing','Marketing'

class LevelChoices(models.TextChoices):

    BEGINNER = 'Beginner','Beginner'

    INTERMEDIATE ='Intermediate','Intermediate'

    ADVANCED ='Advanced','Advanced'

class TypeChoices(models.TextChoices):

    FREE = 'Free','Free'

    PREMIUM = 'Premium','Premium'   


class Courses(BaseClass):

    title = models.CharField(max_length=50)

    description = models.TextField()

    image = models.ImageField(upload_to='course-images/')

    instructor = models.ForeignKey('instructors.Instructors',on_delete=models.CASCADE)
                                    # app.name & model.name


    category = models.CharField(max_length=25,choices=CategoryChoice.choices) # defining  choice as class by inherit textChoices class

    # category = models.CharField(max_length=25,choices=category_choice) #defining choice as list of tuple method

    level = models.CharField(max_length=25,choices=LevelChoices.choices)

    type = models.CharField(max_length=15,choices=TypeChoices.choices)

    fee = models.DecimalField(max_digits=8,decimal_places=2)

    offer_fee = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)

    def __str__(self):

        return f'{self.title}--{self.instructor}'
    
    class Meta:

        verbose_name ='Courses'

        verbose_name_plural ='Courses'

        ordering = ['id']