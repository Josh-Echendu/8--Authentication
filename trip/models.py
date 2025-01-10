from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth import get_user_model # Return the User model that is active in this project.

User = get_user_model()

# Create your models here.

class Trip(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=2)

    # This column can accept a null value
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    # This is associated with the user since we are going to allow users to login
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trips')
    
    def __str__(self):
        return self.city

class Note(models.Model):
    EXCURSIONS = (
        ("event", "Event"),
        ("dining", "Dinning"),
        ("experience", "Experience"),
        ("general", "General"),
    )

    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='notes')
    name = models.CharField(max_length=100)
    description = models.TextField() # TextField can store any amount of strings
    type = models.CharField(max_length=100, choices=EXCURSIONS)

    img = models.ImageField(upload_to='notes', blank= True, null= True) # "upload_to='notes'", this would create a note directory to store th images, "blank= True, null= True", means adding an image is not required
    
    # we want the rating values between 0 to 5
    rating = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(5)]) # 'validator' is use to give precise number of values
    
    def __str__(self):
        return f"{self.name} in {self.trip_id.city}"