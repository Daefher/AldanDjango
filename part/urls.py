from django.urls import path 
from part.views import (
    getParts,
    getAllParts,
    getPart,
    insertPart,
    updatePart,
    cancelPart  
    )

app_name = 'part'

urlpatterns = [
    path('getParts/<companyId>', getParts.as_view(), name='get-all-parts' ),   
    path('getAllParts/<companyId>', getAllParts.as_view(), name='get-all-parts'),
    path('getById/<pk>', getPart.as_view(), name='get-part' ),
    path('insert/', insertPart.as_view(), name='insert-part'),
    path('update/<pk>', updatePart.as_view(), name='update-part'),
    path('cancel/<pk>', cancelPart.as_view(), name='cancel-part' ),
]