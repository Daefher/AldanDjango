from django.urls import path 
from .views import (
   getSalesOrders,
   getAllSalesOrder,
   getSalesOrderById,
   getSalesOrderDtlById,
   getSalesOrdersDtl,
   insertSalesOrder,
   insertSalesOrderDtl,
   updateSalesOrder,
   updateSalesOrderAndDtl,
   updateSalesOrderDtl,
   cancelSalesOrder
)

app_name = 'salesOrder'

urlpatterns = [
    path('getSalesOrders/<companyId>', getSalesOrders.as_view(), name='get-sales-orders' ),  
    path('getCompleteSalesOrders/<companyId>',getAllSalesOrder.as_view(), name='get-all-sales-orders' ),
    path('getById/<pk>', getSalesOrderById.as_view(), name='get-sales-order-by-id'),
    path('insert/', insertSalesOrder.as_view(), name='insert-sales-order'),
    path('update/', updateSalesOrder.as_view(), name='update-sales-order'),
    path('cancel/', cancelSalesOrder.as_view(), name='cancel-sales-order'),
    path('updateFull/', updateSalesOrderAndDtl.as_view(), name='update-full-sales-order'),
    path('dtl/getById/<pk>', getSalesOrderDtlById.as_view(), name='get-sales-order-dtl-by-id'),
    path('dtl/getAll/<pk>', getSalesOrdersDtl.as_view(), name='get-all-sales-order-dtl'),
    path('dtl/insert/', insertSalesOrderDtl.as_view(), name='insert-sales-order-dtl'),
    path('dtl/update/', updateSalesOrderDtl.as_view(), name='update-sales-order-dtl'),
]