dia_de_la_semana=input("escribe el dia de la semana:")
dia_del_mes=int(input("escribe el dia del mes en numero:"))
mes=int(input("escribe el mes en numero:"))
if  dia_del_mes<1 or dia_del_mes>31 :
    print ("el dia del mes es invalido,escribe de nuevo el dia del mes en numero")
if mes<1 or mes>12 :
    print ("el mes es invaldo,escribo el mes en numero de nuevo")
fecha=print(f"{dia_de_la_semana}, {dia_del_mes}/{mes}")
dia_de_la_semana=dia_de_la_semana.lower()
if dia_de_la_semana=="lunes":
    print ("se tomaron examenes de nivel inicial")
    
if dia_de_la_semana=="martes":
    print ("se tomaron examenes de nivel intermedio")
elif dia_de_la_semana=="miercoles":
    print ("se tomaron examenes de nivel avanzado")

if dia_de_la_semana=="lunes" or dia_de_la_semana=="martes" or dia_de_la_semana=="miercoles":
    aprobados=int(input(f"ingresa la cantidas de aprobados de el dia {dia_de_la_semana}:"))
    desaprobados=int(input(f"ingresa la cantidad de desaprobados del dia {dia_de_la_semana}:"))
    total=desaprobados+aprobados
    por_desaprobados=100*(desaprobados/total)
    por_aprobados=100*(aprobados/total)
    print (f"el porcentaje de alumnos aprobados es del {por_aprobados}")
    print (f"el porcentaje de alumnos desaprobados es del {por_desaprobados}")

if dia_de_la_semana=="jueves":
    porcentaje_de_asitencia=int(input("introduce el porcentaje de asistencia:"))
    if porcentaje_de_asitencia>50:
        print ("asistio la mayoria")
    elif porcentaje_de_asitencia<50:
        print ("no asistio la mayoria")
    else:
        print ("asistio la mitad")

if dia_de_la_semana=="viernes":
    if dia_del_mes==1 and mes==1 or dia_del_mes==1 and mes==7:
        print ("empezando el ciclo") 
        alumnos=int(input("escribe la cantidad de alumnos ingresados del nuevo ciclo:"))
        arancel_x_alumno=int(input("ingresa el arancel que debe pagar cada alumno :$"))
        print(f"el total de ingresos por los pagos de alumnos es de ${arancel_x_alumno*alumnos}")