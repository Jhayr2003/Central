from django.contrib import admin
from .models import *

#TABLA CATEGORIA
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('id', 'nombre')
    list_display_links = ('nombre',)
    #list_filter = ('')
    list_per_page = 15 

#TABLA PROMOCION
@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    list_display = ('id', 'descripcion', 'descuento')
    list_display_links = ('descripcion',)
    #list_filter = ('')
    list_per_page = 15   

#TABLA METODOPAGO
@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    search_fields = ('id',)
    list_display = ('id', 'nombre')
    list_display_links = ('nombre',)
    #list_filter = ('')
    list_per_page = 15   

#TABLA Usuario
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'apellido')
    list_display = ('nombre', 'apellido', 'telefono', 'correo')
    list_display_links = ('nombre',)
    #list_filter = ('')
    list_per_page = 15   

#TABLA PROVEEDOR 
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('id', 'nombre', 'telefono', 'correo')
    list_display_links = ('nombre',)
    #list_filter = ('')
    list_per_page = 15   

#TABLA PRODUCTO
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('id', 'nombre', 'descripcion', 'precio', 'categoria')
    list_display_links = ('nombre',)
    list_filter = ('categoria',)
    list_per_page = 15    

#TABLA PEDIDO
@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    search_fields = ('cliente',)
    list_display = ('id', 'cliente', 'total', 'metodo_pago', 'estado', 'fecha')
    list_display_links = ('cliente',)
    list_filter = ('estado', 'metodo_pago')
    list_per_page = 15

#TABLA DETALLE PEDIDO
@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_display = ('id', 'pedido', 'producto', 'cantidad', 'precio_unitario')
    list_display_links = ('pedido',)
    #list_filter = ('')
    list_per_page = 15 

#TABLA COMENTARIO
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    search_fields = ('producto', 'cliente')
    list_display = ('id','cliente', 'producto', 'comentario', 'valoracion')
    list_display_links = ('cliente',)
    list_filter = ('valoracion',)
    list_per_page = 15 

#TABLA BOLETA
@admin.register(Boleta)
class BoletaAdmin(admin.ModelAdmin):
    search_fields = ('cliente', 'pedido')
    list_display = ('id', 'cliente', 'pedido', 'total', 'fecha_emision')
    list_display_links = ('cliente',)
    #list_filter = ('')
    list_per_page = 15 