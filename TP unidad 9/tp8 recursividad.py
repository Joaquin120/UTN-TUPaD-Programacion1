#ejercicio 1
print ("ejercicio 1")
def factorial(n):
    if n == 0:
        return 1
    else:
        return (n*factorial(n-1))

def mostrarfactorial(n):
    for i in range (1,n+1):
        print (f"el factorial de {i} es {factorial(i)}:")
    return ("")



try:
    n=int(input("ingresa un numero para hacer factorial:"))
    if n<0:
        print (0/0)
    else:
        print (mostrarfactorial(n))
except:
    print ("no valido")


print ("")
#ejercicio 2
print ("ejercicio 2")


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(hasta):
    for i in range(hasta+1):
        print(f"Fibonacci({i}) = {fibonacci(i)}")
    return ("")


try:
    n=int(input("ingresa un numero para hacer la serie de fibonachi : "))
    if n<0:
        print (0/0)
    else:
        print (mostrar_fibonacci(n))
except:
    print ("no valido")
print ("")



#ejercicio 3
print ("ejercicio 3")


def potencia(base,exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)



try:
    n=int(input("introduce el numero base : "))
    exp=int(input("introduce el exponente : "))
    print (f'{n}^{exp} = {potencia(n,exp)}')
except:
    print ("no valido")
print ("")

print ("")
#ejercicio 4
print ("ejercicio 4")

def decimal_a_binario(n):
    # Caso base: si el número es 0 o 1, retorna ese número como cadena
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        # Llamada recursiva y concatenamos el residuo (n % 2) al resultado
        return decimal_a_binario(n // 2) + str(n % 2)

n=int(10)
resultado = decimal_a_binario(n)
print(f'El número {n} en binario es: {resultado}')


print ("")
#ejercicio 5
print ("ejercicio 5")


print ("")
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])


palabra = "somos"
print(es_palindromo(palabra))

palabra2 = "casa"
print(es_palindromo(palabra2)) 


print ("")
#ejercicio 6
print ("ejercicio 6")


print ("")
def suma_digitos(n):
    if n == 0:
        return 0
    return n % 10 + suma_digitos(n // 10)

print(suma_digitos(1234)) 
print(suma_digitos(9))     
print(suma_digitos(305)) 

print ("")
#ejercicio 7
print ("ejercicio 7")


print("")
def contar_bloques(n):

    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print(contar_bloques(5)) 
print(contar_bloques(3))  
print(contar_bloques(1)) 


print ("")
#ejercicio 8
print ("ejercicio 8")

print ("")
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:

        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

print(contar_digito(123456, 3))
print(contar_digito(987123, 1))
print(contar_digito(5555, 5)) 
print(contar_digito(123456, 7))  
