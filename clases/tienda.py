class Tienda:
    def __init__(self, nombre, giro):
        self.nombre = nombre
        self.giro = giro
        self.listaProductos = []

    def agregarProducto(self, productoNuevo):
        self.listaProductos.append(productoNuevo)
        return self

    def vendeProducto(self, indiceProducto):
        print(f"Producto Vendido: self.listaProductos[indiceProducto].nombre")
        self.listaProductos.pop(indiceProducto)
        return self

    def ofertaPorCategoriaProducto(self, categoria, porcentaje):
        print("Oferta por Categoria: " + categoria)
        for producto in self.listaProductos:
            if producto.categoria == categoria:
                producto.actualizaPrecio(porcentaje, False)
        return self
    
    def inflacion(self, porcentaje):
        print("Cambio de precio por inflacion")
        for producto in self.listaProductos:
            producto.actualizaPrecio(porcentaje, True)

    def __str__(self):
        imprimir = (self.nombre + "," + self.giro)
        return imprimir