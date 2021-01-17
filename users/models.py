from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(choices=GENDER, max_length=10)
    STATUS = [
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('In A Relationship', 'In A Relationship'),
    ]
    BORNAGAIN = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    middle_name = models.CharField(max_length=50)
    born_again = models.CharField(choices=BORNAGAIN, max_length=5)
    church_name = models.CharField(max_length=100, help_text='What is the name of your church?')
    marital_status = models.CharField(choices=STATUS, max_length=50)
    address = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(null=True, blank=True, help_text="Enter Date In The Format YYYY-MM-DD")
    photo = models.ImageField(upload_to='profile_pics/%Y/%m/%d/')
    favourite_bible_verse = models.TextField(max_length=300, help_text='Not more than 300 words including chapter and verse')
    about_me = models.TextField(max_length=300, help_text='Write something about yourself, not more than 300 words')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


User = get_user_model()

# contact form model


class ContactUs(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    message = models.TextField(max_length=1000, help_text='Write Your Message, not more than 1000 characters')

    def __str__(self):
        return self.full_name


# testimony model

class Testimony(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    testimony = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Testimony from {self.user.username}'


# prayer request
class PrayerRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prayer_points = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Prayer Request from {self.user.username}'
