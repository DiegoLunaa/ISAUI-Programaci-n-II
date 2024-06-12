from producto import Producto
from electronico import Electronico
from alimento import Alimento

producto = Producto("Almohada", 20000, 10)
producto_electronico = Electronico("Notebook", 470000, 10, "HP", "Pavilion")
producto_alimento = Alimento("Manzanas", 500, 50, "10/06/2024")

print("Información del producto:")
producto.mostrar_info()

print("\nInformación del producto electrónico:")
producto_electronico.mostrar_info()

print("\nInformación del producto alimenticio:")
producto_alimento.mostrar_info()