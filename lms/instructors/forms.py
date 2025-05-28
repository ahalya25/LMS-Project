from django import forms

from .models import Instructors , AreaofExpertise

class InstructorForm(forms.ModelForm):

    class Meta:

        model =  Instructors

        exclude = ['profile','name','uuid','active_status']        

    widgets = {


        'image' : forms.FileInput(attrs={
                                                     'class' : 'form-control',
                                                     'required' : 'required'}),

        'description' : forms.Textarea(attrs={
                                                     'class' : 'form-control',
                                                     'required' : 'required',
                                                     'rows' : '6' ,
                                                     'cols' : '15'})                                             
    }


    area_of_expertise = forms.ModelChoiceField(queryset=AreaofExpertise.objects.all(),widget=forms.Select(attrs={
                                                                                           
                                                                                           'class': 'forms-select',
                                                                                           'required':'required'}))
                                                     