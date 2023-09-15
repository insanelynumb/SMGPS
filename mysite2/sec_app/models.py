from django.db import models
from django.contrib.auth.models import User
class Movement(models.Model):
    start_location = models.CharField(max_length=100)
    destination_location = models.CharField(max_length=100)
    start_department = models.CharField(max_length=100)
    destination_department = models.CharField(max_length=100)
    name_of_item = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    purpose_of_movement = models.TextField()
    Level_one_approval = models.CharField(max_length=50, choices=[
        ('cecon2ser@gmail.com', 'Rachana Pandey'),
        ('dcegmhx@gmail.com', 'Ashok Kumar Pandey'),
    ], default='rachu01gautam02@gmail.com')
    Level_two_approval = models.CharField(max_length=50, choices=[
        ('cecon2ser@gmail.com', 'Rachana Pandey'),
        ('dcegmhx@gmail.com', 'Ashok Kumar Pandey'),
    ], default='rachu01gautam02@gmail.com')
    approval_person_name = models.CharField(max_length=100)


    def __str__(self):
        return f"Movement from {self.start_location} to {self.destination_location}"

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

