# Ejemplo de POO

# CREAR UNA CLASE

class Perro: 
    # Constructor
    # asignamos los valores de los atributos si queremos, si no quedan como none
    def __init__(self, n, c, r, t):
        # Propiedades o Atributos
        self.tamaño = t
        self.edad = 0
        self.raza = r
        self.color = c
        self.nombre = n

    # Métodos
    def ladrar(self):
        print("{} está ladrando".format(self.nombre))
        
    def comer(self):
        print("{} está comiendo".format(self.nombre))
        
    def jugar(self):
        print("{} está jugando".format(self.nombre))
    
    def cambiar_nombre(self, nombre):
        self.nombre = nombre
        print("El perro ahora se llama {}".format(nombre))
    
    def get_nombre(self):
        return self.nombre

    def set_edad(self, edad):
        self.edad = edad
        print("{} ahora tiene {}".format(self.nombre, self.edad))
    
    def cumpleaños(self):
        self.edad = self.edad + 1
        print("{} ahora tiene {}".format(self.nombre, self.edad))


# INSTANCIAR OBJETO 1
# Para instanciar un objeto, declaro una variable instanciando a un objeto de la clase Perro.
mi_perro = Perro("Jorge", "Negro", "Doberman", "Grande")


# INSTANCIAR OBJETO 2
mi_perro2 = Perro("Rex", "Blanco", "Lobo", "Mediano") 



# Una vez instanciado, podemos acceder a las propiedades y llamar a métodos del objeto.

print("Acciones perro1:")
mi_perro.comer()
print(mi_perro.raza)

mi_perro.cambiar_nombre("Carlos")
print(mi_perro.nombre)
mi_perro.cumpleaños()


print("Acciones perro2:")
mi_perro2.jugar()
mi_perro2.set_edad(5)
