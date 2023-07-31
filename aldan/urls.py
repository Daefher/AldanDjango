
from django.contrib import admin
from django.urls import path, include
from core.views import PostView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [  
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name= 'test'),
    #path('api/token', obtain_auth_token, name='obtain-token'),
    #path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('api/', include('dj_rest_auth.urls')),
    path('api/company/', include('company.urls'))   
]