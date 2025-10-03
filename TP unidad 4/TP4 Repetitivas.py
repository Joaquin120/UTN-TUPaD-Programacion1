#Trabajo Practico 4:estructras repetitivas
#ejercicio 1
for ej1 in range(0,100,1):
    print (ej1)
    print ("")
#ejercicio 2
num_entero_ej2=int(input("intruduce un numero entero:"))
num_entero_ej2_str=len(str(num_entero_ej2))
print (f"el numero {num_entero_ej2} tiene {num_entero_ej2_str} digitos")
#ejercicio 3
num_ej3=int(input("ingresa el primer numero"))
num2_ej3=int(input("ingresa el segundo numero"))
total=0
if num_ej3<num2_ej3:
    for i3 in range (num_ej3+1,num2_ej3):
        total=total+i3
elif num_ej3>num2_ej3:
    for i3 in range (num2_ej3+1,num_ej3):
        total=total+i3
print (total)
print ("")
#ejercicio 4
num_ej4=0
num_ej4_2=1
while num_ej4_2!=0:
    num_ej4_2=int(input("escribe un numero:"))
    print ("para terminar con el ciclo ingresa 0")
    num_ej4=num_ej4+num_ej4_2
    print (num_ej4)
    print ("")
#ejercicio 5
import random
num_ej5=int(input("adivina el numero del 0 al 9:"))
num_aleatorio=random.randint(0,9)
intentos_ej5=0
while num_ej5!=num_aleatorio:
    print ("intenta de nuevo")
    num_ej5=int(input("adivina el numero del 0 al 9:"))
    intentos_ej5+=1
print ("adivinaste")
print (f"fueron necesarios {intentos_ej5} para que acertaras")
print ("")
#ejercicio 6
for num_ej6 in range (101,-1,-1):
    if num_ej6%2==0:
        print (num_ej6)
print ("")
#ejercicio 7
numero_usuario7=int(input("ingresa un numero"))
valor_acumulado=0
for i7 in range (0,numero_usuario7+1):
    valor_acumulado+= i7
print (f"la suma de los numeros comprendios entre 0 y {numero_usuario7} es {valor_acumulado}")
#ejercicio 8
num_pares=0
num_impares=0
num_negativos=0
num_positivos=0
num=[]
for contador in range (0,100):
    num.append(int(input("ingresa un numero:")))
    if (num[contador])%2==0:
        num_pares=num_pares+1
    else:
        num_impares=num_impares+1
    if num[contador]>0:
        num_positivos=num_positivos+1
    elif num[contador]<0:
        num_negativos=num_negativos+1
print (f"los numeros dados por el usuario son:{num}")
print ("")
print (f"hay {num_positivos} num_positivos")
print (f"hay {num_negativos} num_negativos")
print (f"hay {num_pares} numeros pares y {num_impares} numeros inmpares")
print ("")
#ejercicio 9
total_ej9=0
for i9 in range (0,100):
    num_ej9=int(input("ingresa un numero"))
    total_ej9=total_ej9+num_ej9
print (f"la medio de todos los numeros introducidos es {total_ej9/100}")
print ("")
#ejercicio 10
num_ej10=int(input("introduce un numero para invertirlo:"))
str_de_num=str(num_ej10)
longitud_de_num=len(str_de_num)
print (str_de_num[::-1])