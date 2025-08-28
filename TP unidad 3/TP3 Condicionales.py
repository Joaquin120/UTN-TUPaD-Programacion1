#Práctico 3: Estructuras condicionales
#actividad 1
edad=int(input("escribe tu edad:"))
if edad>=18:
    print ("eres mayor de edad")
else:
    pass

print ("")

#actividad 2
nota_a2=int(input("escribe tu calificacion del 0 a 10:"))
if nota_a2>=0 and nota_a2<6:
    print ("desaprobado")
elif nota_a2>=6 and nota_a2<=10:
    print ("aprobado")
else:
    pass
print ("")

#actividad 3
num_par_a3=int(input("escribe un numero par:"))
if num_par_a3%2==0:
    print("ha ingresado un numero par")
else:
    num_par_a3=int(input("por favor ingrese un numero par"))
print ("")

#actividad 4
edad_a3=int(input("ingresa tu edad:"))
if edad_a3<12:
    print ("eres nino/a")
elif edad_a3>=12 and edad_a3<18:
    print ("eres adolecente")
elif edad_a3>=18 and edad_a3<30:
    print ("eres un adulto/a joven")
elif edad_a3>30:
    print ("eres un adulto/a")
else:
    pass
print ("")
#acticidad 5
contraseña_a5=len(input("escribe una contraseña de entre 8 y 14 caracteres:"))
if contraseña_a5>=8 and contraseña_a5<=14:
    print ("Ha ingresado una contraseña correcta")
else:
    print (input("ingrese una contaseña correcta entre 8 y 14 caracteres:"))
print ("")
#actividad 6
from statistics import mode, median, mean
import random
numeros_aleatorios= [random.randint(1,100) for i in range (50)]
print (numeros_aleatorios)
moda=mode(numeros_aleatorios)
promedio_6=mean(numeros_aleatorios)
mediana=median(numeros_aleatorios)
print(f"la media de numeros aleatorios es {promedio_6}")
print(f"la moda de numeros aleatorios es {moda}")
print(f"la mediana de los numeros aleatorios es {mediana}")
if promedio_6>mediana and mediana>moda:
    print ("hay sesgo positivo")
elif promedio_6<mediana and mediana<moda:
    print ("hay sesgo negativo")
else:
    print ("no hay sesgo")
print ("")
#ejercicio 7
palabra_a7=input("escribe una palabra o frase:")
ultima_letra_a7=palabra_a7[-1]
ultima_letra_a7=ultima_letra_a7.lower()

if ultima_letra_a7=="a" or ultima_letra_a7=="e" or ultima_letra_a7=="i" or ultima_letra_a7=="o" or ultima_letra_a7=="u":
    print (palabra_a7+"!")
else:
    print (palabra_a7)
print("")
#ejercicio 8
nombre_a8=input("escribe tu nombre:")
num_a8=int(input("ingresa el numero 1,2 o 3:"))
if num_a8==1:
    print (nombre_a8.upper())
elif num_a8==2:
    print (nombre_a8.lower())
elif num_a8==3:
    print (nombre_a8.title())
else:
    pass
print ("")
#ejercicio 9
maganitud_a9=int(input("ingresa la magnitud de un terrmoto:"))
if maganitud_a9<3:
    print ("Muy leve (imperceptible)")
elif maganitud_a9>=3 and maganitud_a9<4:
    print ("Leve (ligeramente perceptible)")
elif maganitud_a9>=4 and maganitud_a9<5:
    print ("Moderado (sentido por personas, perogeneralmente no causa daños)") 
elif maganitud_a9>=5 and maganitud_a9<6:
    print ("Fuerte (puede causar daños en estructuras débiles)")  
elif maganitud_a9>=6 and maganitud_a9<7:
    print ("Muy Fuerte (puede causar daños significativos)")
elif maganitud_a9>=7:
    print ("Extremo (puede causar graves daños a gran escala")
print ("")
#ejercicio 10
hemisferio=input("escribe si te encuentras en el hemisferio norte o sur:")
hemisferio=hemisferio.lower()
mes_a10=input("en que mes del año estas?:")
mes_a10=mes_a10.lower()
dia_a10=int(input("ingresa el dia del mes en el que estas:"))
if dia_a10>=21 and dia_a10<=31 and mes_a10=="diciembre" or dia_a10>=1 and dia_a10<=31 and mes_a10=="enero" or dia_a10>=1 and dia_a10<=28 and mes_a10=="febrero" or dia_a10>=1 and dia_a10<=20 and mes_a10=="marzo":
    if hemisferio=="norte":
        print ("te encuentras en invierno")
    elif hemisferio=="sur":
        print ("te encuentras en verano")
elif dia_a10>=21 and dia_a10<=31 and mes_a10=="marzo" or dia_a10>=1 and dia_a10<=30 and mes_a10=="abril" or dia_a10>=1 and dia_a10<=31 and mes_a10=="mayo" or dia_a10>=1 and dia_a10<=20 and mes_a10=="junio":
    if hemisferio=="norte":
        print ("te encuentras en primavera")
    elif hemisferio=="sur":
        print ("te encuentras en otoño")
elif dia_a10>=21 and dia_a10<=30 and mes_a10=="junio" or dia_a10>=1 and dia_a10<=31 and mes_a10=="julio" or dia_a10>=1 and dia_a10<=31 and mes_a10=="agosto" or dia_a10>=1 and dia_a10<=20 and mes_a10=="septiembre":
    if hemisferio=="norte":
        print ("te encuentras en verano")
    elif hemisferio=="sur":
        print ("te encuentras en invierno")
elif dia_a10>=21 and dia_a10<=30 and mes_a10=="septiembre" or dia_a10>=1 and dia_a10<=31 and mes_a10=="octubre" or dia_a10>=1 and dia_a10<=30 and mes_a10=="noviembre" or dia_a10>=1 and dia_a10<=20 and mes_a10=="diciembre":
    if hemisferio=="norte":
        print("te encuentras en otoño")
    elif hemisferio=="sur":
        print("te encuentras en primavera")
else:
    pass