from producto import Producto

class Alimento(Producto): # Clase hija 'Alimento'
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad) # Llamo el constructor de la clase padre
        self.fecha_expiracion = fecha_expiracion
    
    # Get adicional para la clase hija
    def getFechaExpiracion(self):
        return self.fecha_expiracion
    
    def mostrar_info(self):
        super().mostrar_info() # Llamo el metodo mostrar info de la clase padre
        # Añado los atributos de alimento
        print(f"La fecha de expiración del producto es: {self.getFechaExpiracion()}")
    