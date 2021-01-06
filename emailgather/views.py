from django.shortcuts import render
from . forms import InputForm 

def index(request): 
    context ={} 
    context['form']= InputForm() 
    return render(request, "index.html", context) 

def expose(request):
 	email = request.POST.get('email_id')
 	passward = request.POST.get('password_id')
 	print(email,passward)
 	return render(request, "expose.html")