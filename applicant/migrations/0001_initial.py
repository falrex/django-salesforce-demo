# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import salesforce.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant__c',
            fields=[
                ('id', salesforce.fields.SalesforceAutoField(primary_key=True, verbose_name='ID', serialize=False, db_column='Id', auto_created=True)),
                ('FirstName', salesforce.fields.CharField(max_length=200)),
                ('MiddleName', salesforce.fields.CharField(max_length=200)),
                ('LastName', salesforce.fields.CharField(max_length=200)),
                ('CivilStatus', salesforce.fields.CharField(max_length=200)),
                ('MobileNumber', salesforce.fields.CharField(max_length=200)),
                ('TelephoneNumber', salesforce.fields.CharField(max_length=200)),
                ('PermanentAddress', salesforce.fields.CharField(max_length=200)),
                ('PresentAddress', salesforce.fields.CharField(max_length=200)),
                ('EmailAddress', salesforce.fields.EmailField(max_length=200)),
                ('Gender', salesforce.fields.CharField(max_length=200)),
                ('Birthdate', salesforce.fields.DateField()),
                ('Citizenship', salesforce.fields.CharField(max_length=200)),
                ('EducationAttainments', salesforce.fields.CharField(max_length=200)),
                ('AchievementsCertifications', salesforce.fields.CharField(max_length=200)),
                ('Skills', salesforce.fields.CharField(max_length=200)),
                ('CurrentPreviousManager', salesforce.fields.CharField(max_length=200)),
                ('CurrentPreviousPosition', salesforce.fields.CharField(max_length=200)),
                ('CurrentPreviousCompany', salesforce.fields.CharField(max_length=200)),
                ('CurrentPreviousDateEnded', salesforce.fields.CharField(max_length=200)),
                ('CurrentPreviousDateStarted', salesforce.fields.CharField(max_length=200)),
                ('AvailabilityOfEmployment', salesforce.fields.DateField()),
                ('PositionApplyingFor', salesforce.fields.CharField(max_length=200)),
            ],
        ),
    ]
