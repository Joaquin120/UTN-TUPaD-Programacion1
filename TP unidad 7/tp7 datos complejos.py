#FUNCIONES
def lista_de_keys(listas):          #funcion para crear una lista que contenga solamente las keys de un diccionario
    return listas.keys()            #usado en actividad 3

def conteo_frases(frase,list_frase):
    lon_lista=len(list_frase)
    dic_frase_y_conteo={}
    for i in range (0,lon_lista):
        x=list_frase.count(list_frase[i])      #funcion que crea un diccionario con los palabras de una lista y cuantas veces se repiten 
        dic_frase_y_conteo[list_frase[i]]=x    #ejercicio 4
    return dic_frase_y_conteo

def crear_tuplas(lon_tupla):    #para crear una tupla de cualquier longitud 
    listas_temporales=[]
    for i in range (0,lon_tupla):
        permitir=True
        while permitir:
            x=input(f"")
            try:
                x=int(x)
                permitir=False
            except:
                print ("pone un numero entero")              
        listas_temporales.append(x)
    tupla_final=tuple(listas_temporales)
    return tupla_final

def añadir_producto(producto):
    producto_temporal=input("ingresa el producto que queres añadir")
    producto[producto_temporal]=0
    

def añadir_mas_stock(producto,diccionario):
    x=input(f"añadi unidades de {producto}")
    try:
        x=int(x)
        if x==0:
            x=int("")
        diccionario[producto]=x
    except:
        print ("para añadir stock tenes que poner un numero natural")
    
    return diccionario
def agenda():
    agenda={}
    agenda={
        ("lunes","10:00"):"reunion",("lunes","15:00"):"clases de ingles",
        ("martes","13:00"):"clases de matematica",("martes","15:00"):"clases de ingles",
        ("jueves","11:00"):"reunion",
        ("viernes","16:00"):"clases de ingles"
        }
    return agenda

def buscar_en_agenda(agenda):
    dia=input("ingresa el dia para buscar")
    hora=input("ingresa la hora del dia")
    tupla_temporal=(dia,hora)
    if tupla_temporal in agenda:
        
        return (agenda[tupla_temporal])
    else:
        print (tupla_temporal)
        print ("ese dia y hora no estan registrados")
def invertir_diccionario(orginal):
    valores=orginal.values()
    llaves=orginal.keys()
    valores=list(valores)
    llaves=list(llaves)
    invertido={}
    for i in range(0,5):
        invertido[valores[i]]=llaves[i]
    return invertido



#ACTIVIDADES
print ("Actividad 1")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
print ("")
precios_frutas["Naranja"]=1200                      #añadir frutas y precios a la lista
precios_frutas["Banana"]=1500
precios_frutas["Pera"]=2300
print (precios_frutas)
print ("Actividad 2")
precios_frutas["Banana"]=1330
precios_frutas["Manzana"]=1700        #añadir frutas y cambiar precios
precios_frutas["Melon"]=2800
print ("")
print ("actividad 3")
lista_frutas=lista_de_keys(precios_frutas)
print(lista_frutas)
print ("")
print ("actividad 4")
print ("crear almacenaiento para consultar numero de telefonos")
agenda_telefonica={}
for i in range (0,5,1):
    nombre_clave=input("ingresa un nombre:")
    Permitir=True
    while Permitir==True:
        numero_telefonico=input("ingresa el numero telefonico correspondiente")     
        try:
            longitud_numero=len(numero_telefonico)
            numero_telefonico=int(numero_telefonico)
            if longitud_numero==10:
                agenda_telefonica[nombre_clave]=numero_telefonico
                Permitir=False
            else:
                print ("el numero de telefono debe tener 10 digitos")
        except ValueError:
            print ("error (solo usa numero enteros sin espacios)")
print (agenda_telefonica)
print ("")
print ("actividad 5")
frase_usuario=input("ingresa una frase:")
print (conteo_frases(frase_usuario,frase_usuario.split()))
print ("")
print ("actividad 6")
lista_de_nombres=[]
for i in range(0,3):
    nombre=input("ingresa nombre:")
    lista_de_nombres.append(nombre)

tex_de_pedir_nota="ingresa la nota de"
lista_con_tuplas=[]
for i in range (0,3):
    print (f"ingresa la caliiciones de {lista_de_nombres[i]}")
    x=crear_tuplas(3)
    lista_con_tuplas.append(x)
print (lista_con_tuplas[0])
diccionario_alumnos_notas={}
for i in range (0,3):
    diccionario_alumnos_notas[lista_de_nombres[i]]=lista_con_tuplas[i]
print (diccionario_alumnos_notas)
print ("")
print ("actividad 7")
aprobaron_parcial_1={"Joaquin","pedro","Marcelo","Lionel","sergio","agustin"}
aprobaron_parcial_2={"Joaquin","Santiago","Lionel","Miguel","sergio","critian"}
print (f"los alumnos que aprobaron el parcial 1 son:{aprobaron_parcial_1}")
print (f"los alumnos que aprobaron el parcial 2 son:{aprobaron_parcial_2}")
print (f"los alumnos que aprobaron ambos parciales fueron:{aprobaron_parcial_1.intersection(aprobaron_parcial_2)}")
print (f"los alumnos que aprobaron al menos un parcial fueron:{aprobaron_parcial_1.union(aprobaron_parcial_2)}")
print ("")
print ("actividad 8")
productos={"campera":4,"remera":8,"zapatillas":3,"botines":1}
permitir=False
while permitir!=True:
    print ("1:para consultar inverntario")
    print ("2:para consultar un producto en especifico")
    print ("3:para agregar un producto si no esta disponible")
    print ("4:para añadir unidades al stock")
    print ("otro:para salir")
    opcion=input(":")
    match opcion:
        case "1":
            print (productos)
        case "2":
            producto_temporal=input("ingresa el producto que buscas:").lower()
            if producto_temporal in productos:
                print (f"la cantidad {producto_temporal} son {productos[producto_temporal]}")
        case "3":
            producto_temporal=input("ingresa ")
            producto_temporal=producto_temporal.lower()
            if not producto_temporal in productos:
                productos[producto_temporal]=0
        case "4":
            producto_temporal=input("ingresa el producto que quieres añadirle stock:")
            if producto_temporal in productos:
                x=input("ingresa la cantidades que quieres añadir:")
                try:
                    x=int(x)
                    productos[producto_temporal]+=x
                except:
                    print ("error")
        case other:
            permitir=True
print ("")
print ("ejercicio 9")
permitir=False
while permitir != True:
    print ("1:para mostra agenda completa")
    print ("2:para buscar que actividad hay en cierto dia y hora")
    permitir=input(":")
    match permitir:
        case "1":
            print (agenda())
        case "2":
            print (buscar_en_agenda(agenda()))
        case other:
            permitir=True
print ("")    
print ("ejercicio 10")
orginal={
   "Argentina":"Buenos Aires",
   "Estados Unidos":"Washington",
   "Japon":"Tokio",
   "España":"Madrid",
   "Francia":"Paris"
}

print (orginal)
print("")
print (invertir_diccionario(orginal))