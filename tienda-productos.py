class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    def imprimir(self):
        print(f"Producto: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}")
        return self
    def cambiaPrecio(self, precioNuevo):
        self.precio = precioNuevo
        return self
    def aumentarPrecio(self, porcentajeAumento):
        self.precio += self.precio * porcentajeAumento / 100
        print(f"Producto: {self.nombre}, Precio Nuevo: {self.precio}")
        return self
    def __str__(self):
        return f"Producto: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}"

class Tienda:
    def __init__(self, nombre, giro):
        self.nombre = nombre
        self.giro = giro
        self.listaProductos = []
    def __str__(self):
        return f"Tienda: {self.nombre} Giro: {self.giro}"
    def agregarProductos(self, productoNuevo):
        self.listaProductos.append(productoNuevo)
        return self
    def vendeProducto(self, indiceProducto):
        print(f"Producto Vendido: self.listaProductos[indiceProducto].nombre")
        self.listaProductos.pop(indiceProducto)
        return self

tienda1 = Tienda("Plantilin", "Vivero")
print(tienda1)
tienda2 = Tienda("CasaBonita", "Hogar")
print(tienda2)

producto1 = Producto("Arbol _Jade", "Suculenta", 3000);
tienda1.agregarProductos(producto1)
print(producto1)

producto2 = Producto("Sabila", "Aloe", 15000);
tienda1.agregarProductos(producto2)
print(producto2)
producto2.aumentarPrecio(15)




