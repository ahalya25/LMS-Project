# Form, ModelForm

from django import forms

from .models import Courses , CategoryChoice ,LevelChoices , TypeChoices

class CoursesCreateForm(forms.ModelForm):

    class Meta:

        model = Courses

        # fields = ['title','discription','image','category','level','fee','offer_fee']

        # all fields from the form

        # fields ='__all__'

        exclude = ['instructor','uuid','active_status']

        widgets ={

                'title' : forms.TextInput (attrs={

                                                 'class' : 'form-control',

                                                 'placeholder' : 'Enter Course Name',

                                                 'required' : 'required'
                                               }),

                'tags' : forms.TextInput (attrs={

                                                 'class' : 'form-control',

                                                 'placeholder' : 'Enter tags',

                                                 'required' : 'required'
                                               }),


                'image' : forms.FileInput(attrs={
                                                  
                                                  'class' : 'form-control',

                                                  
                                                }) ,

                'description' : forms.Textarea(attrs={

                                                    'class' : 'form-control',

                                                    'placeholder' : 'Enter description',

                                                    'required' : 'required'

                                                }) ,

                'fee' : forms.NumberInput(attrs={
                                                
                                                  'class' : 'form-control',

                                                  'required' : 'required',

                                                  'placeholder' : 'enter course fee',

                                                 })  ,    

                'offer_fee' : forms.NumberInput(attrs={
                                                
                                                  'class' : 'form-control',

                                                  'placeholder' : 'enter offer fee',
                                                        
                                                   }) ,       
        }

    category = forms.ChoiceField (choices=CategoryChoice.choices,widget=forms.Select(attrs={
                                                                                     
                                                                                     'class':'form-select',
                                                                                     'required' : 'required'
                                                                                     }))   

    level = forms.ChoiceField(choices=LevelChoices.choices,widget=forms.Select(attrs={

                                                                                    'class' : 'form-select',
                                                                                    'required' : 'required'

                                                                                     }))
    
    type = forms.ChoiceField(choices=TypeChoices.choices,widget=forms.Select(attrs={

                                                                                    'class' : 'form-select',
                                                                                    'required' : 'required'

                                                                                     }))
    
    def clean(self):
        
        validated_data = super().clean()

        if validated_data.get('fee') and validated_data.get('fee') < 0:
            
            self.add_error('fee','course fee must be graeter than zero')

        if validated_data.get('offer_fee') and validated_data.get('offer_fee') < 0:
            
            self.add_error('offer_fee','course fee must be graeter than zero')    

        # print(validated_data)

        return validated_data

        # return super().clean()

    def __init__(self,*args,**kwargs):

        super(CoursesCreateForm,self).__init__(*args,**kwargs)    

        if not self.instance : 

            self.fields.get('image').widget.attrs['required'] = 'required'   #only one so take widget

