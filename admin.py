from django.contrib import admin
from .models import (
    
    ModeOfEntery, 
    BioData, 
    ResultType, 
    OlevelGrade, 
    JambScore, 
    ChoiceOfCourse, 
    Status,
)



@admin.register(ModeOfEntery)
class ModeOfEnteryAdmin(admin.ModelAdmin):
    pass


@admin.register(BioData) 
class BioDataAdmin(admin.ModelAdmin):
    pass

@admin.register(ResultType)
class ResultTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(OlevelGrade)
class OlevelGradeAdmin(admin.ModelAdmin):
    pass


@admin.register(JambScore)
class JambScoreAdmin(admin.ModelAdmin):
    pass

@admin.register(ChoiceOfCourse)
class ChoiceOfCourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


admin.site.site_header='JYC_concept'

