#--------------------------------------------------------------------------
#Problema01 
nombre = input ("Introduce tu nombre: ")
print ("¡Hola " + nombre + "!")
#----------------------------------------------------------------------------
#Problema02
num = int (input("Cuándos shows musicales ha visto en el último año? "))
if num >=3:
    print("True")
else:
    print("False")
print ("El usuario ha visto ", num , "shows musicales")
#----------------------------------------------------------------------------
#Problema03
#f=sirve para concatenar variables
#int=numero entero, no colocar porque es decimal
num = float(input ("Ingresa un número con decimales: "))
ent = int(input ("Ingrese un numero entero "))
sum = num + ent
print ("El resultado de la suma es: ", sum)
#----------------------------------------------------------------------------
#Problema04
payaso = 112
muñeca = 75
pay = int(input("Ingrese el número de payasos vendidos: ")) #Float: Representa decimales
mun = int(input("Ingrese el número de muñecas vendidas: "))

ventas = pay + mun
sum = payaso + muñeca
pesopay = payaso * pay
pesomun = muñeca * mun
print("El numero de payasos y muñecas vendidas es: ", ventas)
print(f"El peso total del paquete es: " , pesopay + pesomun)
#----------------------------------------------------------------------------
#Problema05
n= int(input("Cuantos números ingresará?: "))
x=0
for i in range(1,n+1):
    print (i)
    x=n*(n+1)/2
print("La suma es: ",x)
#----------------------------------------------------------------------------
#Problema06
edad = int(input("Ingrese su edad: "))
art = int(input("Ingrese cantidad de articulos comprados: "))

if edad >= 18 and art >= 1:
    print ("True")
else:
    print ("False")

print ("El usuario tiene: ", edad, "años y compró ", art, "articulos")
#----------------------------------------------------------------------------
#Problema07
num1 = int(input("Ingrese 1er número: "))
num2 = int(input("Ingrese 2do número: "))


if num1 != num2:
    if num1 < num2:
        print (num2)
    else:
        print (num1)
    pass #esta orden le dice a python que no debe hacer nada
else:
    print ("Ingresar número diferente")  
#----------------------------------------------------------------------------
#Problema08
num1 = float(input("Ingrese 1er número: "))
num2 = float(input("Divisor: "))


if num2 == 0:
    print ("Error")
else:
    print ("La división es: ", num1/num2)
#----------------------------------------------------------------------------
#Problema09
letra = input("Ingrese letra: ")
vocales = ['a','e','i','o','u']

if (len(letra)==1):
    if letra in vocales:
        print ("Es vocal")
    else:
        print ("No es vocal")
    pass
else:
    print ("Datos no puede procesar")
#----------------------------------------------------------------------------
#Problema10 (NO ESTA BIÉN)

año = int(input("Ingrese el año: "))

if año % 400 == 0:
    print ("El año", año, "no es bisiesto")  
else:
    if año % 100 == 0:
       print ("El año", año, "no es bisiesto")       
    else:
        if año % 4 == 0:
            print ("El año", año, "si es bisiesto")  
        
print ('El año si es bisiesto ', (año))
#----------------------------------------------------------------------------
#Problema11
edad = int(input("Que edad tienes?: "))

if edad < 4:
    print ("Entrada gratis")
if edad >= 4 and edad < 18:
        print ("Ud. debe pagar 5 soles")
if edad >= 18:
            print ("Ud. debe pagar 10 soles")
#----------------------------------------------------------------------------
#Problema12

list = ["Mi", "mami", "es", "muy", "linda"]
list.reverse()
print(list)
#----------------------------------------------------------------------------
#Prolema13 (NO ESTA BIEN)

lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
print ("La lista original es: ", lista)

del(lista)[0]   
del(lista)[4]  
del(lista)[5]  

print(lista)
#----------------------------------------------------------------------------
#Prolema14







