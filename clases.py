class Restaurant:

    def agregar_restaurant(self, nombre):
        self.nombre = nombre #atributo de instancia

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}')

#instanciar la clase 
restaurant = Restaurant()
restaurant.agregar_restaurant('pizzeria Colombia')
restaurant.mostrar_informacion()

restaurant2 = Restaurant()
restaurant2.agregar_restaurant('Hamburguesa Express')
restaurant2.mostrar_informacion()


#Mostrar la informacion 
print(f'Nombre Restaurant: {restaurant.nombre}')
print(f'Nombre Restaurant: {restaurant2.nombre}')