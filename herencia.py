class Animal:
    def __init__(self):
        self.edad = None
        self.especie = None
        self.pelaje = None

    def comer(self):
        print("El animal está comiendo")

    def reproducirse(self):
        print("El animal se está reproduciendo")


# al crear la clase hija le pasamos como paramentro en el constructor , el nombre de la clase padre
class Perro(Animal): 
    # Constructor
    # asignamos los valores de los atributos si queremos, si no quedan como none
    def __init__(self):
        # Propiedades o Atributos
        super().__init__()
        self.tamaño = None
        self.raza = None
        self.color = None
        self.nombre = None

    # Métodos
    def ladrar(self):
        print("{} está ladrando".format(self.nombre))
        
        
    def jugar(self):
        print("{} está jugando".format(self.nombre))

    def check_hambre(self, hambre):
        if hambre:
            self.comer()
        else:
            print("{}no esta tiene hambre".format(self.nombre))

mi_perro = Perro()
print(mi_perro.nombre)  
mi_perro.check_hambre(True)
    
