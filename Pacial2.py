# seleccionaremos nuestros principales objetivos que maneja la tienda de niña mary
# estos serian los productos de la tienda , venta que hace co n los productos , y su proveedor el cual le lleva el producto
class Producto:
    def __init__(self, nombre, precio_compra, precio_venta, cantidad):
        self.nombre = nombre
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.cantidad = cantidad

class Venta:
    def __init__(self, fecha, productos):
        self.fecha = fecha
        self.productos = productos
        self.calcular_total()

    def calcular_total(self):
        self.total = sum(producto.precio_venta for producto in self.productos)
# calcularemos 
class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

class Tienda:
    def __init__(self):
        self.productos = []
        self.ventas = []
        self.proveedores = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def realizar_venta(self, productos_comprados):
        venta = Venta(fecha=datetime.now(), productos=productos_comprados)
        self.ventas.append(venta)
        # Actualizar inventario de la Tienda
        for producto in productos_comprados:
            for producto_tienda in self.productos:
                if producto.nombre == producto_tienda.nombre:
                    producto_tienda.cantidad -= 1

    def recibir_productos(self, proveedor, productos):
        proveedor.agregar_producto(productos)
        # Actualizar inventario de la tienda de Niña mary
        # ...