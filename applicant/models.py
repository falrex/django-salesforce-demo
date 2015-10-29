#from django.db import models
from salesforce import models

# Create your models here.
class Applicant__c(models.Model):
    GENDER = (( 'Male','Male'),('Female','Female'))

	#Personal Information
    FirstName = models.CharField(max_length=200, verbose_name='First Name')
    MiddleName = models.CharField(max_length=200, verbose_name='Middle Name')
    LastName = models.CharField(max_length=200, verbose_name='Last Name')
    CivilStatus = models.CharField(max_length=200, verbose_name='Civil Status')
    MobileNumber = models.CharField(max_length=200, verbose_name='Mobile')
    TelephoneNumber = models.CharField(max_length=200, verbose_name='Landline')
    PermanentAddress = models.TextField(verbose_name='Permanent Address')
    PresentAddress = models.TextField(verbose_name='Present Address')
    EmailAddress = models.EmailField(max_length=200, verbose_name='Email')
    Gender = models.CharField(max_length=200, choices=GENDER)
    Birthdate = models.DateField()
    Citizenship = models.CharField(max_length=200)
    #Other Information
    EducationAttainments = models.TextField(verbose_name='Education')
    AchievementsCertifications = models.TextField(verbose_name='Achievements')
    Skills = models.TextField()
    #Current/Previous Employment
    CurrentPreviousManager = models.CharField(max_length=200, verbose_name='Manager')
    CurrentPreviousPosition = models.CharField(max_length=200, verbose_name='Position')
    CurrentPreviousCompany = models.CharField(max_length=200, verbose_name='Company')
    CurrentPreviousDateEnded = models.CharField(max_length=200, verbose_name='Date Ended')
    CurrentPreviousDateStarted = models.CharField(max_length=200, verbose_name='Date Started')
    #ApplicationInformation
    AvailabilityOfEmployment = models.DateField(verbose_name='Availability of Employment')
    PositionApplyingFor = models.TextField(verbose_name='Position Applying For')

    def __str__(self):
       return "%s %s" % (self.FirstName, self.LastName)
    
    class Meta:
        custom=True
        verbose_name = 'Applicant'
        verbose_name_plural = 'Applicants'