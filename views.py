from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import View
from django.views.generic.edit import View
from django.views.generic import TemplateView
from . models import*
from admit.forms import (
    UserCreationForm,
    BioDataForm, 
    ModeOfEnteryForm, 
    ResultTypeForm, 
    OlevelGradeForm, 
    JambScoreForm, 
    ChoiceOfCourseForm
)


  
class BioDataForm(CreateView):
    form_class = BioDataForm
    success_url = reverse_lazy('entry')
    template_name = 'register.html'
    
    

class ModeOfEnteryForm(CreateView):
    form_class = ModeOfEnteryForm 
    success_url = reverse_lazy('result')
    template_name = 'register.html'
 

class ResultTypeForm(CreateView):
    form_class = ResultTypeForm 
    success_url = reverse_lazy('olevel')
    template_name = 'admissionportal/resultype.html'


class OlevelGradeForm(CreateView):
    form_class = OlevelGradeForm 
    success_url = reverse_lazy('jambscore')
    template_name = 'admissionportal/olevel.html'

class JambScoreForm(CreateView):
    form_class = JambScoreForm 
    success_url = reverse_lazy('choice')
    template_name = 'admissionportal/jambscore.html'
    

class ChoiceOfCourseForm(CreateView):
    form_class = ChoiceOfCourseForm 
    success_url = reverse_lazy('completreg')
    template_name = 'admissionportal/choice.html'
    


def registerPage(request):
    form = UserCreationForm()
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}        
    return render(request, 'admissionportal/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'admissionportal/login.html', context)
    
    
def Home(request):
    return render(request, 'home.html')



def Admission_Portal(request):
    	return render(request,'admissionportal/index-2.html')


def About(request):
    return render(request, 'about.html')

class ApplicationPage(TemplateView):
    template_name = 'admissionportal/apply.html'
    
    

class CompletReg(TemplateView):
    template_name = 'admissionportal/completreg.html'








