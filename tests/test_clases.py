import pytest
from Aplicaciones.APP.models import (
    Categoria, Promocion, MetodoPago, Usuario, Proveedor, Producto,
    Pedido, DetallePedido, Comentario, Boleta
)

@pytest.mark.django_db
def test_creacion_categoria():
    categoria = Categoria.objects.create(nombre="Categoría Test")
    assert categoria.nombre == "Categoría Test"

@pytest.mark.django_db
def test_creacion_promocion():
    promocion = Promocion.objects.create(
        descripcion="Promoción Test",
        descuento=15.00,
        fecha_inicio="2024-11-22T00:00:00Z",
        fecha_fin="2024-12-31T23:59:59Z"
    )
    assert promocion.descripcion == "Promoción Test"
    assert promocion.descuento == 15.00

@pytest.mark.django_db
def test_creacion_metodo_pago():
    metodo_pago = MetodoPago.objects.create(nombre="Tarjeta de Crédito")
    assert metodo_pago.nombre == "Tarjeta de Crédito"

@pytest.mark.django_db
def test_creacion_usuario():
    usuario = Usuario.objects.create(
        correo="test@correo.com",
        nombre="Luis",
        apellido="Pérez",
        telefono="999222111",
        contraseña="contradeprueba"
    )
    assert usuario.correo == "test@correo.com"
    assert usuario.nombre == "Luis"
    assert usuario.apellido == "Pérez"

@pytest.mark.django_db
def test_creacion_proveedor():
    proveedor = Proveedor.objects.create(
        nombre="Proveedor Test",
        contacto="Proveedor Contacto",
        telefono="987654321",
        correo="proveedor@test.com"
    )
    assert proveedor.nombre == "Proveedor Test"
    assert proveedor.correo == "proveedor@test.com"

@pytest.mark.django_db
def test_creacion_producto():
    categoria = Categoria.objects.create(nombre="Categoría Test")
    proveedor = Proveedor.objects.create(
        nombre="Proveedor Test",
        correo="proveedor@test.com"
    )
    promocion = Promocion.objects.create(
        descripcion="Promoción Test",
        descuento=20.00,
        fecha_inicio="2024-11-22T00:00:00Z",
        fecha_fin="2024-12-31T23:59:59Z"
    )
    producto = Producto.objects.create(
        nombre="Producto Test",
        descripcion="Descripción Test",
        precio=100.00,
        proveedor=proveedor,
        stock=10,
        categoria=categoria,
        promocion=promocion
    )
    assert producto.nombre == "Producto Test"
    assert producto.precio == 100.00

@pytest.mark.django_db
def test_creacion_pedido():
    metodo_pago = MetodoPago.objects.create(nombre="Tarjeta de Crédito")
    usuario = Usuario.objects.create(
        correo="cliente@test.com",
        nombre="María",
        apellido="López",
        telefono="123456789",
        contraseña="password123"
    )
    pedido = Pedido.objects.create(
        cliente=usuario,
        total=500.00,
        estado="confirmado",
        metodo_pago=metodo_pago
    )
    assert pedido.cliente == usuario
    assert pedido.total == 500.00
    assert pedido.estado == "confirmado"

@pytest.mark.django_db
def test_creacion_detalle_pedido():
    categoria = Categoria.objects.create(nombre="Categoría Test")
    proveedor = Proveedor.objects.create(
        nombre="Proveedor Test",
        correo="proveedor@test.com"
    )
    producto = Producto.objects.create(
        nombre="Producto Test",
        descripcion="Descripción Test",
        precio=100.00,
        proveedor=proveedor,
        stock=10,
        categoria=categoria
    )
    metodo_pago = MetodoPago.objects.create(nombre="Tarjeta de Crédito")
    usuario = Usuario.objects.create(
        correo="cliente@test.com",
        nombre="María",
        apellido="López",
        telefono="123456789",
        contraseña="password123"
    )
    pedido = Pedido.objects.create(
        cliente=usuario,
        total=500.00,
        metodo_pago=metodo_pago
    )
    detalle = DetallePedido.objects.create(
        pedido=pedido,
        producto=producto,
        cantidad=3,
        precio_unitario=100.00
    )
    assert detalle.pedido == pedido
    assert detalle.producto == producto
    assert detalle.cantidad == 3

@pytest.mark.django_db
def test_creacion_comentario():
    categoria = Categoria.objects.create(nombre="Categoría Test")
    proveedor = Proveedor.objects.create(
        nombre="Proveedor Test",
        correo="proveedor@test.com"
    )
    producto = Producto.objects.create(
        nombre="Producto Test",
        descripcion="Descripción Test",
        precio=100.00,
        proveedor=proveedor,
        stock=10,
        categoria=categoria
    )
    usuario = Usuario.objects.create(
        correo="cliente@test.com",
        nombre="María",
        apellido="López",
        telefono="123456789",
        contraseña="password123"
    )
    comentario = Comentario.objects.create(
        cliente=usuario,
        producto=producto,
        comentario="Muy buen producto",
        valoracion=5
    )
    assert comentario.comentario == "Muy buen producto"
    assert comentario.valoracion == 5

@pytest.mark.django_db
def test_creacion_boleta():
    metodo_pago = MetodoPago.objects.create(nombre="Tarjeta de Crédito")
    usuario = Usuario.objects.create(
        correo="cliente@test.com",
        nombre="María",
        apellido="López",
        telefono="123456789",
        contraseña="password123"
    )
    pedido = Pedido.objects.create(
        cliente=usuario,
        total=500.00,
        metodo_pago=metodo_pago
    )
    boleta = Boleta.objects.create(
        pedido=pedido,
        igv=18.00,
        total=500.00,
        cliente=usuario,
        cliente_nombre="María",
        cliente_apellido="López"
    )
    assert boleta.pedido == pedido
    assert boleta.cliente == usuario
    assert boleta.total == 500.00