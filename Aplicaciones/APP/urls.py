from django.urls import path
from Aplicaciones.APP.views import * 

urlpatterns = [
    path('', PromocionListView.as_view(), name  = 'gestion_promocion'),
    path('login/', LoginListView.as_view(), name  = 'gestion_login'),
]
