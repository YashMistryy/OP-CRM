from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, RegexValidator
from django.utils.translation import gettext_noop

# Create your models here.
class UserProfile(models.Model):
    """Model definition for UserProfile."""
    user = models.OneToOneField(User, unique=True, db_index=True, related_name='profile', on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d*$',
        message="Phone number must start with '+' (optional) followed by digits (0-9) only.",
    )
    phone_number = models.CharField(validators=[phone_regex], blank=True, null=True, max_length=50)
    resident_address = models.TextField(blank=True, null=True)
    address_postal_code = models.CharField(max_length=20 , blank=True, null=True)
    language = models.CharField(blank=True, max_length=255, db_index=True)
    year_of_birth = models.IntegerField(blank=True, null=True, db_index=True)
    GENDER_CHOICES = (
        ('m', ('Male')),
        ('f', ('Female')),
        # Translators: 'Other' refers to the student's gender
        ('o', ('Other/Prefer Not to Say'))
    )
    gender = models.CharField(
        blank=True, null=True, max_length=6, db_index=True, choices=GENDER_CHOICES
    )
    LEVEL_OF_EDUCATION_CHOICES = (
        ('p', gettext_noop('Doctorate')),
        ('m', gettext_noop("Master's or professional degree")),
        ('b', gettext_noop("Bachelor's degree")),
        ('a', gettext_noop("Associate degree")),
        ('hs', gettext_noop("Secondary/high school")),
        ('jhs', gettext_noop("Junior secondary/junior high/middle school")),
        ('el', gettext_noop("Elementary/primary school")),
        # Translators: 'None' refers to the student's level of education
        ('none', gettext_noop("No formal education")),
        # Translators: 'Other' refers to the student's level of education
        ('other', gettext_noop("Other education"))
    )
    level_of_education = models.CharField(
        blank=True, null=True, max_length=6, db_index=True,
        choices=LEVEL_OF_EDUCATION_CHOICES
    )    
