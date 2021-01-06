from django import forms 
  
# creating a form  
class InputForm(forms.Form): 
  
    email = forms.CharField(max_length = 200) 
    passward = forms.CharField(widget = forms.PasswordInput()) 