class Restaurant:

    def __init__(self, nombre, categoria, precio):
        self.nombre = nombre #atributo de instancia y pasa automaticamente al constructor
        self.categoria = categoria #atributo de instancia y pasa automaticamente al constructor
        self.__precio = precio #atributo de instancia y pasa automaticamente al constructor // Default: public, PROTECTED_ , PRIVATE__

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, categoria: {self.categoria}, precio: {self.__precio}')

    #GETTERS Y SETTERS: son metodos genericos que permiten acceder a los atributos privados de una clase, para poder modificarlos o obtener su valor, se utilizan para proteger los datos de una clase, para que no se modifiquen desde fuera de la clase, se pueden utilizar para validar los datos antes de modificarlos, o para realizar alguna accion antes de obtener su valor, se utilizan para encapsular los datos de una clase, para que no se puedan modificar desde fuera de la clase, 
    #GETTERS Y SETTERS - Get = obtiene un valor, SET = agrega un valor 

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

#instanciar la clase 
restaurant = Restaurant('pizzeria Colombia', 'comida italiana', 50000)
#restaurant.__precio = 80000 # no sera posible modificarlo con PRIVATE__ ya que es un atributo privado, solo se puede modificar desde dentro de la clase 
restaurant.mostrar_informacion()
restaurant.set_precio(80000) # se puede modificar con el metodo SETTER
precio =restaurant.get_precio()
print(precio) # se puede obtener con el metodo GETTER


restaurant2 = Restaurant('Hamburguesa Express', 'comida rapida', 30000)
restaurant2.mostrar_informacion()
restaurant2.set_precio(60000)
precio =restaurant2.get_precio()
print(precio)

#constructor: es una funcion que se ejecuta automaticamente al instanciar una clase 
#abstraccion: son datos necesarios de una clase, que datos son necesarios en esta clase y que datos son necesarios en esta abstraccion
