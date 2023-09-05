from django.db import models


# Create your models here.

class studentdetails(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    phone_number=models.IntegerField()
    email=models.CharField(max_length=255)
    course=models.TextField()
    address=models.TextField()
    image = models.ImageField(upload_to='images/', null=True)
    
    

    # Add other fields as needed