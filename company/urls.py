from django.urls import path 
from company.views import (
    getCompany,
    getCompanyFiles
    )

app_name = 'company'

urlpatterns = [
    path('get/<pk>', getCompany.as_view(), name='get-company' ),
    path('companyFiles/get/<companyId>', getCompanyFiles.as_view(), name='get-files-company' )
]