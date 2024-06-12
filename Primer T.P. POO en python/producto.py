class Producto:
    def __init__(self, nombre, precio, cantidad): # Inicializo los atributos
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Defino gets para los atributos
    def getNombre(self):
        return self.nombre
    
    def getPrecio(self):
        return self.precio
    
    def getCantidad(self):
        return self.cantidad
    
    # Hago un metodo para mostrar la información completa
    def mostrar_info(self):
        print(f"El nombre del producto es: {self.getNombre()}")
        print(f"El precio del producto es: $ {self.getPrecio()}")
        print(f"La cantidad del producto es: {self.getCantidad()}")
