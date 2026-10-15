class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo de instancia y pasa automaticamente al constructor
        self.categoria = categoria #atributo de instancia y pasa automaticamente al constructor
        self._precio = precio #atributo de instancia y pasa automaticamente al constructor // Default: public, PROTECTED_

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, categoria: {self.categoria}, precio: {self._precio}')

#instanciar la clase 
restaurant = Restaurant('pizzeria Colombia', 'comida italiana', 50000)

print(restaurant._precio)
restaurant._precio = 80000
restaurant.mostrar_informacion()


restaurant2 = Restaurant('Hamburguesa Express', 'comida rapida', 30000)

print(restaurant2._precio)
restaurant2._precio = 60000
restaurant2.mostrar_informacion()

#encapsulamiento: es una forma de proteger los datos de una clase, para que no se puedan modificar desde fuera de la clase, se puede hacer con el uso de metodos genericos (getters y setters) y con el uso de propiedades (property)