from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Company(models.Model):
    name = models.CharField(null=True,max_length=255)
    location = models.CharField(max_length=255,null=True, blank=True)
    established_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.ForeignKey(Company,null=True,blank=True, on_delete=models.CASCADE, related_name='employees')

    department = models.CharField(_("current job department"), max_length=50)    
    ROLE_CHOICES = [
        ('intern', 'Intern'),
        ('employee', 'Employee'),
        ('lead', 'Lead'),
        ('manager', 'Manager'),
        ('chief_officer', 'Chief Officer'),
    ]
    job_role = models.CharField(_("current job role"), choices=ROLE_CHOICES, max_length=50)    
    immediate_manager = models.CharField(_("immediate manager of employee"),null=True, blank=True,max_length=50) 
    WORKING_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('on_leave', 'On Leave'),
        ('on_notice_period', 'On Notice Period'),
        ('terminated', 'Terminated'),
    ]   
    working_status  = models.CharField(_("working status"), choices=WORKING_STATUS_CHOICES,null=True, blank=True, max_length=50)    
    hire_date =models.DateField(("hiring date"), null=True, blank=True,max_length=50)    
    reason_for_resign = models.CharField(_("reason for resignation"), null=True, blank=True,max_length=50)    
    pancard_number = models.CharField(_("identification number for eg. pancard no."), null=True, blank=True,max_length=50)    
    

