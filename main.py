from clases.producto import Producto
from clases.tienda import Tienda

tienda1 = Tienda("Plantilin", "Vivero")
print(tienda1)
tienda2 = Tienda("CasaBonita", "Hogar")
print(tienda2)

producto1 = Producto("Arbol de Jade", "Suculenta", 3000);
tienda1.agregarProducto(producto1)
print(producto1)

producto2 = Producto("Sabila", "Aloe", 15000);
producto3 = Producto("Sabila2", "Aloe", 18000)
tienda1.agregarProducto(producto2)
tienda1.agregarProducto(producto3)
print(producto2)
print(producto3)
print(tienda2)

producto2.actualizaPrecio(15, True)
producto1.actualizaPrecio(20, False)

tienda1.inflacion(25)
tienda1.ofertaPorCategoriaProducto("Aloe", 25)




