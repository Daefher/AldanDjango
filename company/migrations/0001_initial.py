# Generated by Django 4.2.3 on 2023-07-31 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('companyId', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('fileStoragePath', models.CharField(max_length=100, null=True)),
                ('ImagesPath', models.CharField(max_length=100, null=True)),
                ('ftpUserName', models.CharField(max_length=100, null=True)),
                ('ftpPassword', models.CharField(max_length=100, null=True)),
                ('canceledBy', models.IntegerField(null=True)),
                ('canceledDateTime', models.DateTimeField(null=True)),
                ('canceled', models.BooleanField(default=False)),
                ('cancelable', models.BooleanField()),
                ('createdBy', models.BigIntegerField()),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
                ('payPalClientId', models.CharField(max_length=200, null=True)),
                ('payPalClientSecret', models.CharField(max_length=200, null=True)),
                ('paypalPartnerArrtId', models.CharField(max_length=200, null=True)),
                ('contactEmail', models.EmailField(max_length=254, null=True)),
                ('smtpServer', models.CharField(max_length=100, null=True)),
                ('smtpPort', models.IntegerField(null=True)),
                ('smtpEmail', models.EmailField(max_length=254, null=True)),
                ('smtpPassword', models.CharField(max_length=50, null=True)),
                ('smtpEnabled', models.BooleanField()),
                ('companyWebSite', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('logoUrl', models.CharField(max_length=50, null=True)),
                ('facebookUrl', models.CharField(max_length=100, null=True)),
                ('instagramUrl', models.CharField(max_length=100, null=True)),
                ('whatsappUrl', models.CharField(max_length=100, null=True)),
                ('youtubeUrl', models.CharField(max_length=100, null=True)),
                ('contactPhoneNumber', models.CharField(max_length=50, null=True)),
                ('system_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='companyPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageName', models.CharField(max_length=128, null=True)),
                ('pageTypeId', models.BigIntegerField(null=True)),
                ('pageKeyWords', models.TextField()),
                ('canceledBy', models.BigIntegerField()),
                ('canceledDateTime', models.DateTimeField(null=True)),
                ('canceled', models.BooleanField()),
                ('createdBy', models.BigIntegerField(null=True)),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
                ('cancelable', models.BooleanField()),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='companyPageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sectionTitle', models.CharField(max_length=128, null=True)),
                ('SectionSubtitle', models.CharField(max_length=128, null=True)),
                ('sectionDescription', models.TextField(null=True)),
                ('sectionPosition', models.IntegerField(null=True)),
                ('sectionFontColor', models.CharField(max_length=128, null=True)),
                ('sectionBGColor', models.CharField(max_length=128, null=True)),
                ('sectionCss', models.CharField(max_length=128, null=True)),
                ('canceledBy', models.BigIntegerField()),
                ('canceledDateTime', models.DateTimeField(null=True)),
                ('canceled', models.BooleanField()),
                ('createdBy', models.BigIntegerField(null=True)),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
                ('cancelable', models.BooleanField()),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('companyPageid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.companypage')),
            ],
        ),
        migrations.CreateModel(
            name='companyFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('fileName', models.CharField(max_length=500)),
                ('filePath', models.TextField(null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('canceledBy', models.BigIntegerField()),
                ('canceledDateTime', models.DateTimeField(null=True)),
                ('canceled', models.BooleanField()),
                ('createdBy', models.BigIntegerField(null=True)),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
                ('cancelable', models.BooleanField()),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
        migrations.CreateModel(
            name='companyAuthorizedDomain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
                ('canceledBy', models.BigIntegerField()),
                ('canceledDateTime', models.DateTimeField(null=True)),
                ('canceled', models.BooleanField()),
                ('createdBy', models.BigIntegerField(null=True)),
                ('createdDateTime', models.DateTimeField(auto_now_add=True)),
                ('cancelable', models.BooleanField()),
                ('companyId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
            ],
        ),
    ]
