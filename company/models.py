from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class company(models.Model):
    system_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    companyId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    fileStoragePath = models.CharField(max_length=100, null=True)
    ImagesPath = models.CharField(max_length=100, null=True)
    ftpUserName = models.CharField(max_length=100, null=True)
    ftpPassword = models.CharField(max_length=100, null=True)
    canceledBy = models.IntegerField(null=True)
    canceledDateTime = models.DateTimeField(null=True)
    canceled = models.BooleanField(default=False)
    cancelable = models.BooleanField()
    createdBy = models.BigIntegerField()
    createdDateTime = models.DateTimeField(auto_now_add=True)
    payPalClientId = models.CharField(max_length=200, null=True)
    payPalClientSecret = models.CharField(max_length=200, null=True)
    paypalPartnerArrtId = models.CharField(max_length=200, null=True)
    contactEmail = models.EmailField(null=True)
    smtpServer = models.CharField(max_length=100, null=True)
    smtpPort = models.IntegerField(null=True)
    smtpEmail = models.EmailField(null=True)
    smtpPassword = models.CharField(max_length=50, null=True)
    smtpEnabled = models.BooleanField()
    companyWebSite = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    logoUrl = models.CharField(max_length=50, null=True)
    facebookUrl = models.CharField(max_length=100, null=True)
    instagramUrl = models.CharField(max_length=100, null=True)
    whatsappUrl = models.CharField(max_length=100, null=True)
    youtubeUrl = models.CharField(max_length=100, null=True)
    contactPhoneNumber = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.name}"
    
class companyAuthorizedDomain(models.Model):
    companyId = models.ForeignKey(company, on_delete=models.CASCADE)
    domain = models.CharField(max_length=100)
    active = models.BooleanField()
    canceledBy = models.BigIntegerField()
    canceledDateTime = models.DateTimeField(auto_now_add=False, null=True)
    canceled = models.BooleanField()
    createdBy = models.BigIntegerField(null=True)
    createdDateTime =  models.DateTimeField(auto_now_add=True)
    cancelable = models.BooleanField()

    def __str__(self):
        return f"{self.domain}"

class companyFile(models.Model):
    companyId = models.ForeignKey(company, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    fileName = models.CharField(max_length=500)
    filePath = models.TextField(null=True)
    title = models.CharField(max_length=100, null=True)
    subtitle = models.CharField(max_length=100, null=True)
    canceledBy = models.BigIntegerField()
    canceledDateTime = models.DateTimeField(auto_now_add=False, null=True)
    canceled = models.BooleanField()
    createdBy = models.BigIntegerField(null=True)
    createdDateTime =  models.DateTimeField(auto_now_add=True)
    cancelable = models.BooleanField()

    def __str__(self):
        return f"{self.name}"    

class companyPage(models.Model):
    companyId = models.ForeignKey(company, on_delete=models.CASCADE)
    pageName = models.CharField(max_length=128, null=True)
    pageTypeId = models.BigIntegerField(null=True)
    pageKeyWords =  models.TextField()
    canceledBy = models.BigIntegerField()
    canceledDateTime = models.DateTimeField(auto_now_add=False, null=True)
    canceled = models.BooleanField()
    createdBy = models.BigIntegerField(null=True)
    createdDateTime =  models.DateTimeField(auto_now_add=True)
    cancelable = models.BooleanField()   

class companyPageData(models.Model):
    companyId = models.ForeignKey(company, on_delete=models.CASCADE)
    companyPageid = models.ForeignKey(companyPage, on_delete=models.CASCADE)
    sectionTitle =models.CharField(max_length=128, null=True)
    SectionSubtitle =models.CharField(max_length=128, null=True)
    sectionDescription= models.TextField(null=True)
    sectionPosition=models.IntegerField( null=True)
    sectionFontColor=models.CharField(max_length=128, null=True)
    sectionBGColor=models.CharField(max_length=128, null=True)
    sectionCss=models.CharField(max_length=128, null=True)
    canceledBy = models.BigIntegerField()
    canceledDateTime = models.DateTimeField(auto_now_add=False, null=True)
    canceled = models.BooleanField()
    createdBy = models.BigIntegerField(null=True)
    createdDateTime =  models.DateTimeField(auto_now_add=True)
    cancelable = models.BooleanField()