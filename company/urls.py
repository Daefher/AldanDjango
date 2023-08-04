from django.urls import path 
from company.views import (
    getCompany,
    getCompanyFiles,
    getByHostName,
    updateCompany
    )

app_name = 'company'

urlpatterns = [
    path('get/<pk>', getCompany.as_view(), name='get-company' ),
    path('GetByHostName/<companyWebSite>', getByHostName.as_view() , name='get-by-hostname'),
    path('companyFiles/get/<companyId>', getCompanyFiles.as_view(), name='get-files-company' ),
    path('update/', updateCompany.as_view(), name='update-company')
]