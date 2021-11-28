
#Problema3
from math import pi

r = float(input('Escriba el radio del circulo: '))

area = pi * r ** 2

print ('El area del circulo es: {}'.format(area))

#Problema4
class Rectangulo:
    def __init__(self, ancho, largo):
        self.ancho=ancho
        self.largo=largo
    def area(self):
        area=self.largo*self.ancho
        return area
    def perimetro(self):
        perimetro=(self.largo*2)+(self.ancho*2)
        return perimetro
r1=Rectangulo(4,2)
area=r1.area()
perimetro=r1.perimetro()
print("El area es", area)
print("El perimetro es: ", perimetro)

#Problema5
class Persona:
    def __init__(self, Nombre, Edad, NumRegistro, Nota):
        self.Nombre=Nombre
        self.Edad=Edad
        self.NumRegistro=NumRegistro
        self.Nota=Nota

    def __str__(self):
        return 'Nombre: {}\nEdad: {}\nNumero de Registro: {}\nNota: {}'.format(self.Nombre, self.Edad, self.NumRegistro, self.Nota)

shirley = Persona('Shirley', '29', '61564436','19')

print (shirley)


#Problema8
def triangulo_pascal (filas):
    fila = [1]
    cero = [0]

    for i in range (filas):
        print (fila)

        fila = [i + d for i , d in zip(fila + cero, cero + fila)]

triangulo_pascal(5)


