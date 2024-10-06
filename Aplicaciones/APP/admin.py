from django.contrib import admin
from .models import *

#TABLA CATEGORIA
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass    

#TABLA PROMOCION
@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    pass   

#TABLA METODOPAGO
@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    pass   

#TABLA Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass   

#TABLA PROVEEDOR 
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    pass   

#TABLA PRODUCTO
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass    

#TABLA PEDIDO
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    pass 

#TABLA DETALLE PEDIDO
@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    pass 

#TABLA COMENTARIO
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass 

#TABLA BOLETA
@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    pass 