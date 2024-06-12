from producto import Producto

class Electronico(Producto): # Clase hija 'Electronico'
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        super().__init__(nombre, precio, cantidad) # Llamo el constructor de la clase padre
        self.marca = marca
        self.modelo = modelo
    
    # Getters adicionales para la clase hija
    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo

    def mostrar_info(self):
        super().mostrar_info() # Llamo el metodo mostrar info de la clase padre
        # Añado los atributos de electronico
        print(f"La marca del producto es: {self.getMarca()}")
        print(f"El modelo del producto es: {self.getModelo()}")
