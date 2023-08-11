from django.db import models
from django.contrib.auth import get_user_model
from part.models import part
from company.models import company
User = get_user_model()

# Create your models here.

class partQty(models.Model):
    companyId = models.ForeignKey(company, on_delete=models.CASCADE)
    partQtyId = models.AutoField(primary_key=True)
    partId = models.ForeignKey(part, on_delete=models.CASCADE)
    onHandQty = models.DecimalField(max_digits=18, decimal_places=2)
    canceledBy = models.IntegerField(null=True,blank=True)
    canceledDateTime = models.DateTimeField(null=True,blank=True)
    canceled = models.BooleanField(default=False)
    cancelable = models.BooleanField()