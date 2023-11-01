
from django import forms
from .models import Student
from.models import stdlogin
from.models import admlogin,usertimings


class StudentForm(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={"name":"username",'class':" col-form-label","type":'text',"placeholder":"enterusername"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"name":"password",'class':" col-form-label","type":'password',"placeholder":"enterpassword" }))
    mobile=forms.CharField(widget=forms.TextInput(attrs={"name":"mobile",'class':" col-form-label","type":'number',"placeholder":"enterusername"}))
    emailid=forms.CharField(widget=forms.TextInput(attrs={"name":"emailid",'class':" col-form-label","type":'email',"placeholder":"enterpassword" }))
    adress=forms.CharField(widget=forms.TextInput(attrs={"name":"adress",'class':" col-form-label","type":'textarea','rows':"5","columns":"5","placeholder":"enterusername"}))
    
    class Meta:
      model=Student
      
      fields="__all__"
      
class Studentlogin(forms.ModelForm):
    class Meta:
      model=stdlogin
      
      fields="__all__"
class adminlogin(forms.ModelForm):
    class Meta:
      model=admlogin
      
      fields="__all__"
class UserTime(forms.ModelForm):
   class Meta:
      model=usertimings
      fields="__all__"     
      
      
    