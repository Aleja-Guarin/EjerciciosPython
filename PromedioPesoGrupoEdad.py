#PROGRAMA PARA CALCULAR PROMEDIO DE PESOS DE ACUERDO A GRUPO DE EDAD

"""Entradas
edad
peso
"""

contninos = 0
contjovenes = 0
contadultos = 0
contviejos = 0
pesoninos = 0
pesojovenes = 0
pesoadultos = 0
pesoviejos = 0
print ("\n\t Estadística de Pesos\t\n")
reiniciar= "s"
while reiniciar == "s":
    edad = int(input ("Ingrese la edad de la persona "))
    peso = float(input ("Ingrese el peso de la persona "))


    """Procesos
    Identificar el grupo al que pertenece el dato (niño, joven, adulto, viejo)
    """
    if (edad > 0 and edad <= 13):
            contninos = contninos + 1
            pesoninos = pesoninos + peso
    elif (edad > 13 and edad <= 30):
            contjovenes = contjovenes + 1
            pesojovenes = pesojovenes + peso
    elif (edad > 30 and edad <= 60):
            contadultos = contadultos + 1
            pesoadultos = pesojovenes + peso
    else:
            contviejos = contviejos + 1
            pesoviejos = pesoviejos + peso
            
    reiniciar= input ("Desea ingresar otra persona, s/n?")


    "SALIDAS"
        
    print ("El numero de Niños ingresado fue = ", contninos)
    print ("El numero de Jóvenes ingresado fue = ", contjovenes)
    print ("El numero de Adultos ingresado fue = ", contadultos)
    print ("El numero de Viejos ingresado fue = ", contviejos)

if (contninos == 0):
    contninos = 1
if (contjovenes == 0):
    contjovenes = 1
if (contadultos == 0):
    contadultos = 1
if (contviejos == 0):
    contviejos = 1

print ("El promedio de peso de Niños fue = ", pesoninos / contninos)
print ("El promedio de peso de Jóvenes  fue = ", pesojovenes / contjovenes)
print ("El promedio de peso de Adultos fue = ", pesoadultos / contadultos)
print ("El promedio de peso de Viejos  fue = ", pesoviejos / contviejos)
