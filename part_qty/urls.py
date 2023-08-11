from django.urls import path 
from .views import (
    getPartQtyByPartid,
    getPartQtyById,
    insertPartQty
)

app_name = 'partQty'

urlpatterns = [
    path('getPartQtyByPartId/', getPartQtyByPartid.as_view(), name='get-by-partId' ), 
    path('getById/<pk>', getPartQtyById.as_view(), name='get-by-id' ), 
    path('insert/', insertPartQty.as_view(), name='insert' )
]