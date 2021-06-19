class Producto:
    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
    
    def cambiaPrecio(self, precioNuevo):
        self.precio = precioNuevo
        return self

    def actualizaPrecio(self, porcentaje, aumento):
        if aumento:
            self.precio += self.precio * porcentaje
            print(f"Producto: {self.nombre}, {porcentaje}% aumento de precio. Precio Nuevo: {self.precio}")
        else:
            self.precio -=  self.precio * porcentaje / 100
            print(f"Producto: {self.nombre}, {porcentaje}% bajo de precio. Precio Nuevo: {self.precio}")
        return self
    
    def imprimir(self):
        print(f"Producto: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}")
        return self
    
    def __str__(self):
        return f"Producto: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}"