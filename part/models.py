from django.db import models
from django.contrib.auth import get_user_model
from company.models import company

User = get_user_model()

class part(models.Model):
    companyId = models.ForeignKey(company, on_delete=models.CASCADE)
    partId = models.AutoField(primary_key=True, serialize=True)
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    payPaltoken = models.CharField(max_length=200, null=True)
    canceledBy = models.IntegerField(null=True)
    canceledDateTime = models.DateTimeField(null=True)
    canceled = models.BooleanField(default=False)
    cancelable = models.BooleanField()
    createdBy = models.BigIntegerField()
    createdDateTime = models.DateTimeField(auto_now_add=True)
    unitCost = models.DecimalField(max_digits=18, decimal_places=2)
    partType = models.CharField(max_length=50, null=True)
    imageFile = models.CharField(max_length=512, null=True)
    category = models.CharField(max_length=50, null=True)
    subcategory = models.CharField(max_length=50, null=True)

class partQty(models.Model):
    companyId = models.ForeignKey(company, on_delete=models.CASCADE)
    partQtyId = models.AutoField(primary_key=True)
    partId = models.ForeignKey(part, on_delete=models.CASCADE)
    onHandQty = models.DecimalField(max_digits=18, decimal_places=2)
    canceledBy = models.IntegerField(null=True)
    canceledDateTime = models.DateTimeField(null=True)
    canceled = models.BooleanField(default=False)
    cancelable = models.BooleanField()

class partTran(models.Model):
    companyId = models.ForeignKey(company, on_delete=models.CASCADE)
    partTranId = models.AutoField(primary_key=True)
    partId = models.ForeignKey(part, on_delete=models.CASCADE)
    tranQty = models.DecimalField(max_digits=18, decimal_places=2)
    tranType = models.CharField(max_length=50)
    canceledBy = models.IntegerField(null=True)
    canceledDateTime = models.DateTimeField(null=True)
    canceled = models.BooleanField(default=False)
    cancelable = models.BooleanField()