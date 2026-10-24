from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.


class Registration(models.Model):

    name = models.CharField(max_length=50)
    number = PhoneNumberField(_("Phone Number"),unique=True , region ='IN')
    st_id = models.CharField(
        max_length =7,
        unique =True,
        validators= [RegexValidator( regex = r'^\d{7,8}$',
                                    message="Enter a Valid 6-7 digit Student number")])
    uni_id = models.CharField(
        max_length=13,
        unique=True,
        validators= [RegexValidator(
            regex= r'^\d{13}$',
            message = "Enter a valid University number"
        )]
    )

    GENDER_CHOICE =[
        ('M','MALE'),
        ('F','FEMALE'),
        ('O','OTHERS'),
        ('N','PREFER NOT TO SAY'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)

    YEAR_CHOICE =[
        ('2','2nd YEAR'),
        ('3','3rd YEAR'),
        ('4','4th YEAR'),
    ]
    year = models.CharField(max_length=1,choices=YEAR_CHOICE)


    BRANCH_CHOICE = [
        ('CSE', 'CSE'),
        ('AIML', 'CSE (AI & ML)'),
        ('DS', 'CSE (Data Science)'),
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('CSIT', 'CS-IT'),
        ('ECE', 'Electronics & Communication'),
        ('EN', 'Electronics & Instrumentation'),
        ('OTH', 'Others'),
    ]
    branch = models.CharField(max_length=4,choices=BRANCH_CHOICE)

    RESIDENCE_CHOICE = [
        ('D', "Day Scholar"),
        ('H',"Hosteller"),
    ]
    residence = models.CharField(max_length=1,choices=RESIDENCE_CHOICE)


    email = models.EmailField(_("Email Address"), max_length=254)
    password = models.CharField(null=False)
