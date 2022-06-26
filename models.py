from django.db import models
from django.forms import ModelForm


class ModeOfEntery(models.Model):
    entry = (('UTME', 'UTME'),
             ('DE', 'DE'),
             ('PRE-NCE', 'PRE-NCE'),)
    mode_of_entry = models.CharField(max_length=50, choices=entry)
    
    def __str__(self):
        return self.mode_of_entry
    
            
   
class BioData(models.Model):
    surname = models.CharField(max_length=250)
    middlename = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    sex =(
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    )
    gender = models.CharField(max_length=50, choices=sex)
    marital_status =('married', 'single')
    dob = models.DateTimeField()
    phone_number = models.CharField(max_length=12, default='070000000')
    email = models.EmailField()
    nationality = models.CharField(max_length=250, default= 'Nigeria')
    state_of_origin = models.CharField(max_length=250)
    local_govt = models.CharField(max_length=250)
    contact_address = models.CharField(max_length=250)
    mode_of_entry = models.ForeignKey(ModeOfEntery, related_name='entries', on_delete=models.CASCADE)
    
   
    def __str__(self):
        return self.name 
   

class ResultType(models.Model):
    olevel = (
        ('neco', 'NECO'),
        ('waec', 'WAEC'),
        ('nabteb', 'NABTEB'),
        ('gce', 'GCE'),
        )
    result_type = models.CharField(max_length=25, choices=olevel)
    
    
    def __str__(self):
         return self.result_type
    
    
        
class OlevelGrade(models.Model):
    result_type = models.ManyToManyField(ResultType, related_name='results')
    subject = (
        ('ENG', 'ENGLISH'),
        ('MAT', 'MATHEMATICS'),
        ('PHY', 'PHYSICS'),
        ('CHEM', 'CHEMISTRY'),
        ('GEO', 'GEOGRAPHY'),
        ('BIO', 'BIOLOGY'),
        ('CRK', 'CRK'),
        ('IRK', 'IRK'),
        ('CIV', 'CIVIC EDU')
        
    )
    grades = (
        ('A', 'Destintion'),
        ('B', 'Creadit'),
        ('C', 'Pass'),
        ('D', 'Fail'),
        
    )
    subjects = models.CharField(max_length=25, choices=subject)
    grade= models.CharField(max_length=25, choices=grades)
    
    def __str__(self):
        return self.result_type
    
    
     
class JambScore(models.Model):
    reg_number = models.CharField(max_length=12)
    score = models.CharField(max_length=3)
    
    def __str__(self):
        return self.reg_number
    
        
        
    
class ChoiceOfCourse(models.Model):
    courses =(
    ('mat', 'MAT/CSC'),
    ('PHY', 'PYH/CSC'),
)
    course = models.CharField(max_length=25, choices=courses)
    
    def __str__(self):
        return self.course
        
    
          
class Status(models.Model):
    ad_status = (
        ('pending', 'pending'),
        ('progress', 'progress'),
        ('rejected', 'rejected'),
    )
    reg_num = models.CharField(max_length=12)
    admission_status = models.CharField(max_length=10, choices=ad_status, default='pending')
    
    def __str__(self):
        return self.reg_num
        
class Admission_Status(models.Model):
    ADMISSION = (
        ('pending', 'Pending'),
        ('admited', 'Admited'),
        ('reject', 'Rejected'),
    )
    admission = models.CharField(max_length=60, choices=ADMISSION, default='pending')
    candidate = models.ForeignKey(BioData, on_delete=models.CASCADE, related_name='status')                   
    

