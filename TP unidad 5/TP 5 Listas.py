#Trabajo Practico N°4
#ejercicio 1
print ("*ejercicio 1:")
div4=[]
div4=list(range(1,101))
for num in range (0,101):
    if num%4 != 0:
        div4.remove(num)
print (div4)
print ("")
#ejercicio 2
print ("*ejercicio 2:")
lista_ej2=["hola",23,"joaquin",98,True]
longitud_ej2=len(lista_ej2)
lista_ej2.remove(lista_ej2[longitud_ej2-2])
print (lista_ej2)
print ("")
#ejercicio 3
print ("*ejercicio 3:")
lista_vacia_ej3=[]
lista_vacia_ej3.append("hola")
lista_vacia_ej3.append("python")
lista_vacia_ej3.append(3.12)
print (lista_vacia_ej3)
print ("")
#ejercicio 4
print ("*ejercicio 4:")
animales=["perro","gato","conejo","pez"]
animales[1]="loro"
animales[3]="oso"
print (animales)
print ("")
#ejercicio 5
print ("*ejercicio 5:")
print ("en el programa hay una lista a la que luego se le elimina el numero 22 por ser el valor mas grande y despues imprimir la lista")
print ("")
#ejercicio 6
print ("*ejercicio 6:")
lista_ej6=list(range(10,30+1,5))
print (lista_ej6[:2])
print ("")
#ejercicio 7
print ("*ejercicio 7:")
autos= ["sedan","polo","suran","gol"]
autos[1]="motor"
autos[2]="luces"
print (autos)
print ("")
#ejercicio 8
print ("ejercicio 8:")
dobles=[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print (dobles)
print ("")
#ejercicio 9
print ("*ejercicio 9:")
compras=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines"
compras[0].remove("pan")
print (compras)
print ("")
#ejercicio 10
print ("*ejercicio 10:")
lista_anidada=[[15],[True],[25.5,57.9,30.9],[False]]
print (lista_anidada)