with open("productos.txt","w")as productos:
    productos.write("producto:lapiz precio:250 cantidad:5\n")
    productos.write("producto:goma precio:200 cantidad:4\n")
    productos.write("producto:cartuchera precio:400 cantidad:3\n")    #ejercicio 1
    
    
with open("productos.txt","r")as productos:   #ejercicio 2
    lista_temporal=[]
    for producto in productos:
        producto=producto.strip().split(",")
        lista_temporal.append(producto)
    for producto in lista_temporal:
        producto=str(producto)
        lista_final=producto.replace(" ","|")
        print (lista_final)
print ("") #los print("") seran usados para mejorar legibilidad cuando se ejecute el programa
        

with open ("productos.txt","a")as productos:   # ejercicio 3
    
    permitir=False
    while permitir == False:
        while permitir==False:
            producto=input("ingresa un producto para añadirlo:").lower()       #añadiendo producto
            print ("")
            permitir=1
            while permitir==1:
                precio=input("ingresa el precio del producto: $")  #pidiendo el para precio del producto
                print ("")
                try:       #validaciones
                    if precio.isdigit():
                        precio=int(precio)
                    else:
                        precio=float(precio)
                    if precio<0:
                        precio=0/0
                    permitir=False
                except:   #en caso de que no sea un numero mayor o igual a 0
                    print ("no es valido")
            permitir=True
        permitir = False


        while permitir==False:
            cantidad=input("ingresa la cantidad de stock del producto:")    #añadiendo la cantidad
            print ("")
            try:
                if not cantidad.isdigit():
                    cantidad=0/0 #provoco un error para no usar otra cosa que no sea numeros enteros
                else:
                    cantidad=int(cantidad)           #validaciones
                if cantidad<0:
                    cantidad=0/0
                permitir=True
            except:
                print ("input no valido (solo son validos los numeros enteros)")

        texto=f"producto:{producto} precio:{precio} cantidad:{cantidad}\n"
        productos.write(texto)
        permitir=input("ingresa 1 para añadir otro producto caso contrario ingresar cualquier otro caracter o numero:")
        print("")
        if permitir == "1":
            permitir = False
        else:
            permitir = True
#fin ejercicio 3

# ejercicio 4
with open ("productos.txt","r")as productos:
    productos=productos.read()
print (productos)
#
print (" ")
#
productos=productos.split("\n") #convirto productos en lista quitando serparando por el salto de linea
productos.pop()  #en el ejercicio anterio el salto de linea vacio de la anterior linea
#
print (productos)
#
lista_de_productos=[]


for producto in productos:
    diccionario_productos={}
    producto=producto.split()  #separo el producto,el precio y la cantidad en distintos indices
    #
    print (producto)
    #
    for partes in producto:
        partes=partes.split(":")
        clave=partes[0]    #consigo la clave y el valor de las partes para añadirlo al diccionario
        valor=partes[1]
        diccionario_productos[clave]=valor
    lista_de_productos.append(diccionario_productos)
productos=lista_de_productos
#ejercicio 5
permitir=False
while permitir == False:
    usuario=input ("ingresa el nombre del producto que buscas:").lower() #lo paso a minuscula para asegurarme de que encuentre el producto
    print ("")
    for producto in productos: 
        permitir=True
        if usuario in producto["producto"]:   #busca el producto dentro de la lista
            print (producto)
            permitir=True
            break  #para terminar el bucle y permita el print ("ERROR") en caso de ser necesario
        permitir=False #si break no es usado permitir va a ser False y va a ejercutar la siguiente linea
    if permitir !=True:
        print ("ERROR")
    
    print ("")
    permitir=False
    
    permitir = input("ingresa 1 si queres seguir cualquier otro caracter si no quieres seguir: ")
    if permitir == "1":
        permitir = False
print ("")
#ejercicio 6

with open ("productos.txt","w")as archivo:
    for producto in productos:
        producto=str(producto)               #trasformo los elementos de la productos a string para poder escribirlos en archivo.txt y luego-
        archivo.write(f"{producto}\n")       #escribo cada elemento linea por linea
#fin ejercicio 6
#fin Trabajo practico de manejo de archivos