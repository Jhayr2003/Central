from django.urls import path
from Aplicaciones.APP.views import * 
from . import views

urlpatterns = [
    path('', PromocionListView.as_view(), name  = 'gestion_promocion'),
    path('login/', LoginListView.as_view(), name  = 'gestion_login'),
    path('registrarUsuario/', views.registrarUsuario),
    path('validarUsuario/', views.validarUsuario),
    path('pagina_inicio/', pagina_inicio),
    path('cerrar_sesion/', views.cerrar_sesion),
    path('configuracion_usuario/', configuracion_usuario),
    path('datos_personales/', datos_personales),
    path('historial_compras/', views.historial_compras, name='historial_compras'),
    path('editar_usuario/', views.editar_usuario, name='editar_usuario'),
    path('contactos/', Contactos),
    path('Nosotros/', nosotros),
    path('cart/', views.cart_views, name='cart'),
    path('procesar_pago/', procesar_pago),
]
