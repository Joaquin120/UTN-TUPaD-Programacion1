def inprimir_hola_mundo():
    return "hola mundo"        #hacer funcion de hola mundo
def saludar_usuario(usr):
    return f"hola {usr}"   #hacer una funcion que saluda al usuario              #ejercicio 1

def nombre():
    permitir=False
    while permitir!=True:
        nombre=input("ingresa tu nombre:") #funcion para poner nombre        #ejercicio 2 y 3
        if not nombre.isdigit():
            permitir=True
        else:
            print("no valen numeros")
    return nombre

def apellido():
    permitir=False
    while permitir!=True:
        apellido=input("ingresa tu apellido:") #funccion para poner apellido          #ejercicio 3
        if not apellido.isdigit():
            permitir=True
        else:
            print ("no valen numeros")
    return apellido

def edad():
    permitir=False
    while permitir!=True:
        edad=input("ingresa tu edad:")  #funcion para poner edad             #ejercicio 3
        if edad.isdigit():
            edad=int(edad)
            permitir=True
        else:
            print ("usa numeros")
    return edad

def residencia():
    residencia=input("ingresa tu residencia:") #poner residencia           #ejercicio 3
    return residencia

def datos_personales(nombre,edad,apellido,residencia): #funcion para inprimir datos personales               #ejercicio 3
    return f"te llamas {nombre} {apellido} tenes {edad} años y tu lugar de residencia es {residencia}"

def radio_circulo():
    permitir=False
    while permitir==False:
        radio=input("ingresa el radio del circulo en centimetros:")    #funcion que permite al usuario ingresar el radio de un circulo
        if radio.isdigit():                                               #ejercicio 4
            radio=int(radio)
            permitir=True
        elif not radio.isdigit():
            print ("usa solo numeros")

    return radio

def calcular_area_circulo(radio):  #para calcular el area del circulo                     #ejercicio 4
    area_circulo=3.14159*(radio*radio)    #formula para area de circulo: A=πr^2
    return f"el area del circulo es {area_circulo} cm²"

def calcular_perimetro_circulo(radio):
    perimtro_circulo=2*3.14159*radio                  #calcular perimetro del circulo
    return f"el perimetro del circulo es {perimtro_circulo}cm"       #ejercicio 5

def segundos():
    permitir=False
    while permitir==False:
        segundos=input("")
        if not segundos.isdigit():
            print("usa solo numeros para la cantidad de segundos")     #funcion para pedir segundos al usuario
        else:
            segundos=int(segundos)        #ejercicio 5
            permitir=True
    return segundos

def segundos_a_horas(segundos):        #funcion para pasar segundos a goras
    horas=(segundos/60)/60
    return horas

def numero():
    permitir=False
    while permitir==False:
        numero=input("")
        if not numero.isdigit():
            print ("tenes que poner un numero")   #funcion para pedir numero al usuario
        if numero.isdigit:                                #ejercicio 6
            numero=int(numero)
            permitir=True
    return (numero)
    
def tabla_multiplicar(numero):
    print ("")
    for i in range (1,11,1):                      #funcion para hacer una tabla de multiplicar
        print (f"{numero}X{i}={numero*i}")            #ejercicio 6
    return ""

def operaciones_basicas (a,b):
    operacion=(f"{a}+{b}={a+b}  ",f"{a}-{b}={a-b}   ",f"{a}X{b}={a*b}  ",f"{a}/{b}={a/b};")  #funcion para hacer suma,resta,multiplicaion y division adentro de una tupla con sos valores
    return operacion               #ejercicio 7

def peso():
    peso=float(input("ingresa tu peso en KG:"))    #funcion para pedir el peso KG
    return peso          #ejercicio 8              #si se coloca alguna letra tira error
                                                    #no lo corregi debido a que no puedo usar try
def altura():
    altura=float(input("ingresa tu alura en metro(con sus decimales):")) # funcion para pedir lacaltura en metro
    return altura        #ejercicio 8             #si se coloca alguna letra tira error
                                                    #no lo corregi debido a que no puedo usar try

def IMC(peso,altura):              #calculo del IMC
    return peso/(altura*altura)   #ejercicio 8

def celcius():
    celcius=float(input("ingresa los grados celcius:"))     #funcion para pedir al usuario grados celcius
    return celcius        #ejercicio 9

def celcius_a_farenheit(celcius):
    farenheit=celcius*1.8         #funcion para pasar de celcius a farenheit

def calcular_promedio(a,b,c):
    promedio=(a+b+c)/3           #funcion para calcular promedio de tres numeros
    return promedio              #ejercicio 10

print ("ejercicio 1")
print("")
print (inprimir_hola_mundo()) #inprimir una hola mundo
print ("")
print ("ejercicio 2")
print (saludar_usuario(nombre())) #bucle para asegurarse que el usuario no escriba numero

permitir=False
print ("")
print ("ejercicio 3")
print (datos_personales(nombre(),edad(),apellido(),residencia())) #inprimir datos personales
print ("")
print ("ejercicio 4")
print ("vamos a calcular el area de un circulo")
print (calcular_area_circulo(radio_circulo()))
print ("")
print ("vamos a calcular el perimetro de un circulo")
print (calcular_perimetro_circulo(radio_circulo()))
print ("")
print ("ejercicio 5")
print ("ingresa la cantidad de segundos:") 
segundos=segundos()
print (f"{segundos} segundos en horas son {segundos_a_horas(segundos)}")
print ("")
print ("ejercicio 6")
print ("ingresa un numero para hacer la tabla de multiplicar:")
print (tabla_multiplicar(numero()))
print ("")
print ("ejercicio 7")
permitir=False
while permitir==False:
    a=input("ingresa el valor de a:")
    b=input("ingresa el valor de b:")
    if not a.isdigit() or not b.isdigit():
        print ("solo numeros")
    elif a.isdigit() and b.isdigit():
        a=int(a)
        b=int(b)
        permitir=True
print (operaciones_basicas(a,b))
print ("")
print ("ejercicio 8")
print (f"tu IMC es del {IMC(peso(),altura())}")
print ("")
print ("ejercicio 9")
print (celcius_a_farenheit(celcius()))
print ("")
print ("ejercicio 10")
a=int(input("ingresa el valor de a:"))
b=int(input("ingresa el valor de b:"))
c=int(input("ingresa el valor de c:"))
print (f"el promedio de {a},{b} y {c} es {calcular_promedio(a,b,c)}")