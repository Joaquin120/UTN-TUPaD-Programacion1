print ("ejercicio 1")
corrimiento=int(input("ingresa el corrimiento de letras:"))
lugares=["primer","segundo","tercero","cuarto","quinto"]
for i in range (0,5):
    mensaje=""
    texto=input(f"escribe el {lugares[i]} mensaje:")
    num_texto=len(texto)
    for num in range(0,num_texto,1):
        letra=texto[num]
        letra=letra.lower()
        letra=ord(letra)
        if letra==32:
            pass
        else:
            letra=letra+corrimiento
        if letra>122:
            letra=letra-26
        letra=chr(letra)
        mensaje=mensaje+letra
    if i==0:
        mensaje_1=f"el primer mensaje es {mensaje}"
    if i==1:
        mensaje_2=f"el segundo mensaje es {mensaje}"
    if i==2:
        mensaje_3=f"el tercer mensaje es {mensaje}"
    if i==3:
        mensaje_4=f"el cuarto mensaje es {mensaje}"
    if i==4:
        mensaje_5=f"el quinto mensaje es {mensaje}"
print (mensaje_1)
print (mensaje_2)
print (mensaje_3)
print (mensaje_4)
print (mensaje_5)
print ("ejercicio 2")
print ("")
print ("")
nombre=input("como te llamas?:")
import random
p_p_t=["piedra","piedra","papel","tijera"]
marcador_us=0
marcador_maq=0
empate=0
jugar=int(input("quieres jugar? 1 para si, 0 para no:"))
while jugar>=1:
    gana_piedra=0
    gana_papel=0
    gana_tijera=0
    usuario=int(input("oprima 1 para piedra,2 para papel o 3 para tijera:"))
    maquina=random.choice(p_p_t)
    print (f"{nombre}:{p_p_t[usuario]}")
    print (f"maquina:{maquina}")
    if maquina=="piedra":
        num_maquina=1
    elif maquina=="papel":
        num_maquina=2
    elif maquina=="tijera":
        num_maquina=3    
    if usuario==1 and num_maquina==3 or usuario==3 and num_maquina==1:
        gana_piedra=1
    elif usuario==3 and num_maquina==2 or usuario==2 and num_maquina==3:
        gana_tijera=3
    elif usuario==2 and num_maquina==1 or usuario==1 and num_maquina==2:
        gana_papel=2
    if usuario==gana_piedra:
        print (f"gana {nombre}")
        marcador_us=marcador_us+1
    elif num_maquina==gana_piedra:
        print (f"gana maquina")
        marcador_maq=marcador_maq+1
    if usuario==gana_tijera:
        print (f"gana {nombre}")
        marcador_us=marcador_us+1
    elif num_maquina==gana_tijera:
        print (f"gana maquina")
        marcador_maq=marcador_maq+1
    if usuario==gana_papel:
        print (f"gana {nombre}")
        marcador_us=marcador_us+1
    elif num_maquina==gana_papel:
        print (f"gana maquina")
        marcador_maq=marcador_maq+1
    elif num_maquina==usuario:
        empate=empate+1
        print ("empate")
    print (f"{nombre}:{marcador_us}|maquina:{marcador_maq}|empates:{empate}")
    jugar=int(input("si queres seguir jugando presiona 1 si queres salir presiona 0:"))