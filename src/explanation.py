'''
#               python    
Front-end  ->    API ->   objetos   -> DB
Front-end  <-    API ->   objetos   <- DB

'''
#OBJETOS
#POO programación orientada a objetos

'''
class Carro():
//constructor
def __init__(self, modelo, marca, cilindraje, color, asientos):
    self.modelo = modelo
    self.marca = marca
    self.cilindraje = cilindraje
    self.color = color
    self.asientos = asientos

//metodos
def calcular-velocidad():
    //código que calcula velocidad

def calcular-las-RPM():
    //código que calcula rpm

def calcular-aceleracion():
    //código que calcula la aceleración


Instanciar nuevo Objeto Carro llamado Corolla
corolla = Carro('corolla', 'toyota', 2000, 'blanco', 4)
corolla.asientos //4
corolla.velocidad() // 

Atributos:
    modelo: Corolla
    marca: Toyota
    cilindraje: 2000
    color: blanco
    asientos: 4

Metodos
    calcular-velocidad
    calcular-las-RPM
    calcular-aceleracion


Instanciar nuevo objeto Carro llamado Spark
Atributos:
    modelo: Spark
    marca: Chevrolet
    cilindraje: 1.2
    color: negro
    asientos: 4

Metodos
    calcular-velocidad
    calcular-las-RPM
    calcular-aceleracion
'''

class Carro():
#constructor
    def __init__(self, modelo, marca='mercedes', cilindraje=1000):
        self.modelo = modelo
        self.marca = marca
        self.cilindraje = cilindraje

#metodos
    def calcular_velocidad(self, distancia, tiempo):
        return f'{distancia / tiempo}km/h'
    

corolla = Carro('corolla', 'toyota', 2000)
spark = Carro('spark', 'chevrolet')

print(f'marca: {corolla.marca}, modelo: {corolla.modelo}, cilindraje: {corolla.cilindraje} con una velocidad \
de {corolla.calcular_velocidad(488, 15)}')

print(f'spark cilindraje: {spark.cilindraje}')


