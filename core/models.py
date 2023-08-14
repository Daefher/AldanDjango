from django.db import models
from django.contrib.auth import get_user_model
from company.models import company

# Create your models here.

User = get_user_model()

class Post(models.Model):    
    title = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title       

class contactMessage(models.Model):
    companyId = models.ForeignKey(company, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200, null=False, default=None)
    email = models.EmailField(max_length=100, null= False, default=None)
    message = models.TextField(null=False, default=None)
    phoneNumber = models.CharField(max_length=200, null=True, default=None)
    canceledBy = models.IntegerField(null=True)
    canceledDateTime = models.DateTimeField(null=True)
    canceled = models.BooleanField(default=False)
    cancelable = models.BooleanField(default=True)
    createdBy = models.BigIntegerField()
    createdDateTime = models.DateTimeField(auto_now_add=True)    