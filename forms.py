from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import fields
from .models import BioData, ResultType, OlevelGrade, JambScore, ChoiceOfCourse


    
    
    
class BioDataForm(forms.ModelForm):
    class Meta:
        model=BioData
        fields = "__all__"


class ModeOfEnteryForm(forms.ModelForm):
    class Meta:
        fields = "__all__"


class ResultTypeForm(forms.ModelForm):
    class Meta:
        model =ResultType
        fields = "__all__"


class OlevelGradeForm(forms.ModelForm):
    class Meta:
        model = OlevelGrade
        fields = "__all__"


class JambScoreForm(forms.ModelForm):
    class Meta:
        model = JambScore
        fields = "__all__"
        

class ChoiceOfCourseForm(forms.ModelForm):
    class Meta:
        model = ChoiceOfCourse
        fields = "__all__"