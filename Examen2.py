#Problema1

def numeros_divisibles_multiplos (limite_inferior, limite_superior):
    if limite_superior > limite_inferior:

        resultado = []

        for n in range (limite_inferior, limite_superior + 1):
            if n % 7 == 0 and n % 5 == 0:
                resultado.append(n)

        return resultado

    raise ValueError('El limite inferior debe ser menor al limite superior.')

    numeros = numeros_divisibles_multiplos(1500, 2700)

    print (numeros)

    #Problema2

    n = 5

for i in range (1, n + 1):
    for j in range (i):
        print ('* ', end='')
    print ()

for i in range (n - 1, 0, -1):
    for j in range (i):
        print ('* ', end='')
    print ()

    #Problema3
def contar_pares_impares(lista):
    pares, impares = 0,0

    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

numeros = [1,2,3,4,5,6,7,8,9]
resultado = contar_pares_impares(numeros)

print('La cantidad de pares es: %i' % resultado[0])
print('La cantidad de pares es: %i' % resultado[1])

#Problema5
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

for x in range(20):
    print (fib(x))

#Problema6
def contar_digitos_letras (cadena):
    digitos = 0
    letras = 0

    for c in cadena:
        if c.isdigit():
            digitos += 1
        elif c.isalpha():
            letras += 1
        else:
            pass
    
    return letras, digitos

texto = input ('Digite un texto: ')
resultado = contar_digitos_letras(texto)

print ('Cantidad de letras: %i' % resultado[0])
print ('Cantidad de digitos: %i' % resultado[1])

#Problema7
def multiplicar(numeros):
    producto = 1

    for n in numeros:
        producto *= n

    return producto

lista_numeros = [8, 2, 3, -1, 7]
print(multiplicar(lista_numeros))

#Problema8
cadena = '1234abcd'

print (cadena[::-1])

#Problema9
def valores_unicos(lista):
    return list(set (lista))

numeros = [2,3,3,5,7,0,0,1,11,13,13,13]

resultado = valores_unicos(numeros)

print(numeros)
print(resultado)

#Problema10
def es_primo (numero):
    if numero == 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range (2,numero):
            if numero % i == 0:
                return False

        return True
for i in range (1,100):
    print (i, es_primo(i))

#Problema11
def pares(numeros):
    numeros_pares = []

    for n in numeros:
        if n % 2 == 0:
            numeros_pares.append(n)
    
    return numeros_pares

numeros = [1,2,3,4,5,6,7,8,9]

resultado = pares(numeros)

print (numeros)
print(resultado)

#Problema12
def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)
        
print (factorial(5))



