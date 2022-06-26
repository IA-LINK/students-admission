from django.contrib.auth import login
from django.urls import path
from . import views
from . views import (BioDataForm, 
                     ModeOfEnteryForm,
                     ResultTypeForm, 
                     OlevelGradeForm, 
                     JambScoreForm, 
                     ChoiceOfCourseForm,
                     ApplicationPage,
                     CompletReg,
                     )

urlpatterns = [
path('login/', views.loginPage, name="login"),

path('',views.Home,name='home'),    
path('Admission_Portal',views.Admission_Portal,name='Admission_Portal'),
path('apply/', ApplicationPage.as_view(), name='apply'),
path('register/', BioDataForm.as_view(), name='register'),
path('BioData/<str:pk>/',views.BioData,name="BioData"),
path('entry/', ModeOfEnteryForm.as_view(), name='entry'),
path('result/', ResultTypeForm.as_view(), name='result'),
path('olevel/', OlevelGradeForm.as_view(), name='olevel'),
path('jambscore/', JambScoreForm.as_view(), name='jambscore'),
path('choice/', ChoiceOfCourseForm.as_view(), name='choice'),
path('completreg',CompletReg.as_view(), name = 'completreg'),
path('about',views.About,name='About')
]
