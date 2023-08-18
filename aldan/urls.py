
from django.contrib import admin
from django.urls import path, include
from core.views import PostView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

schema_view = get_schema_view(
   openapi.Info(
      title="Aldan API",
      default_version='v1',
      description="Multiple sites one ecommerce",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="daefher@gmail.com"),
      license=openapi.License(name="Aldan"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [      
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #path('', PostView.as_view(), name= 'test'),
    #path('api/token', obtain_auth_token, name='obtain-token'),
    #path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    #path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('login/', include('dj_rest_auth.urls')),
    path('company/', include('company.urls')),  
    path('part/', include('part.urls')),
    path('partQty/', include('part_qty.urls')),
    path('salesOrder/', include('salesOrder.urls'))

]