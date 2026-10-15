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

#crear una clase hijo de restaurant
class Hotel(Restaurant):
    def __init__(self, nombre, categoria, precio):
        super().__init__(nombre, categoria, precio) #llamar al constructor de la clase padre

hotel = Hotel('hotel POO', '5 estrellas', 1000000)
hotel.mostrar_informacion()