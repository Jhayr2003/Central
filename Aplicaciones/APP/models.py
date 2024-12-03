from django.db import models

from django.db import models

class Categoria(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre


class Promocion(models.Model):
    descripcion = models.TextField(blank=True, null=True)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()

    def __str__(self):
        return self.descripcion


class MetodoPago(models.Model):
    nombre = models.TextField()

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    correo = models.EmailField(primary_key=True)
    nombre = models.TextField()
    apellido = models.TextField()
    telefono = models.TextField(blank=True, null=True)
    contraseña = models.TextField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Proveedor(models.Model):
    nombre = models.TextField()
    contacto = models.TextField(blank=True, null=True)
    telefono = models.TextField(blank=True, null=True)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.TextField()
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.TextField(default='pendiente')  # Opciones: pendiente, completado
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    referencia_pago = models.CharField(max_length=100, blank=True, null=True)  # Código de Yape

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.correo}"
    

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle {self.id} - {self.pedido.id}"


class Comentario(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    comentario = models.TextField()
    valoracion = models.IntegerField()

    def __str__(self):
        return f"Comentario {self.id} - {self.cliente.correo}"


class Boleta(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    igv = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cliente_nombre = models.TextField()
    cliente_apellido = models.TextField()

    def __str__(self):
        return f"Boleta {self.id} - {self.cliente.correo}"
