from django.contrib import admin

from .models import Applicant__c

class ApplicantAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'classes': ('wide', 'extrapretty'),
            'fields': (('FirstName','MiddleName', 'LastName'),'CivilStatus',('MobileNumber','TelephoneNumber'),'PermanentAddress','PresentAddress','EmailAddress','Gender','Birthdate','Citizenship')
        }),      
        ('Other Information', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('EducationAttainments','AchievementsCertifications','Skills')
        }),     
        ('Current/Previous Employment', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('CurrentPreviousManager','CurrentPreviousPosition','CurrentPreviousCompany','CurrentPreviousDateEnded','CurrentPreviousDateStarted')
        }),  
        ('Application Information', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('AvailabilityOfEmployment','PositionApplyingFor')
        }),
    )

admin.site.register(Applicant__c, ApplicantAdmin)