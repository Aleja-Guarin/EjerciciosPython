def menu():

    print ('*****Menu Principal*****')
    print('1. Ver Listado')
    print('2. Ver listado filtrado')
    print('3. Agregar Beneficiario')
    print('4. Buscar Beneficiario')
    print('5. Borrar Beneficiario')
    print('6. Salir')

def principal():
   
    menu()
    opcion = input()
    opcion = opcion.upper().strip()

    if opcion == '1':
        ver_lista()    
    elif opcion == '2':
        print("Ingrese la letra inicial de los contactos:")
        buscar_letra=input()
        buscar_lista(buscar_letra)
    elif opcion == '3':
        print("Digite la información del beneficiario a agregar:")
        nombre=input()
        cedula=input()
        celular=input()
        agregar(nombre,cedula,celular)    
    elif opcion == '4':
        print ("Ingrese el nombre y apellido del contacto a buscar:")
        buscar_nombre=input()
        buscar_por_nombre(buscar_nombre)
    elif opcion == '5':
        print("Ingrese la cedula del contacto a borrar:")
        buscar_cedula=input()
        eliminar_cedula(buscar_cedula) 
    else:
        print("Ha salido de la agenda")
    


def agregar(nombre,cedula,celular):
    directorio=[]
    try:
        agenda = open("agenda.txt", "r")
        directorio = agenda.readlines()
        agenda.close()
    except:
        agenda = open("agenda.txt", "w")
        
    if cedula +"\n" in directorio:
        print()
        principal()
    else:
        agenda = open("agenda.txt", "w")
        directorio.append(nombre)
        directorio.append(cedula)
        directorio.append(celular)
        for linea in directorio:
            agenda.write(str(linea.strip()+"\n"))
        agenda.close()
        print("El beneficiario ha sido agregado")
        
    principal()

def ver_lista ():
    print ("Listado de beneficiarios")
    directorio=[]
    try:
        agenda = open("agenda.txt", "r")
        directorio = agenda.readlines()
        agenda.close()
    except:
        agenda = open("agenda.txt", "w")
    if directorio ==[]:
        principal()
    else:
        for linea in directorio:
            print (linea.strip("\n"))
    principal()   

        
def buscar_por_nombre(buscar_nombre):
    directorio=[]
    try:
        agenda = open("agenda.txt", "r")
        directorio = agenda.readlines()
        agenda.close()
    except:
        f = open("agenda.txt", "w")
    if buscar_nombre+"\n" not in directorio:
        principal()
    else:
        for linea in directorio:
            if linea == buscar_nombre +"\n":
                
                indice = directorio.index(linea)
                print (directorio[indice].strip("\n"))
                print (directorio[indice+1].strip("\n"))
                print (directorio[indice+2].strip("\n"))
        principal ()
    
def eliminar_cedula(buscar_cedula):
    directorio=[]
    try:
        agenda = open("agenda.txt", "r")
        directorio = agenda.readlines()
        agenda.close()
    except:
        agenda = open("agenda.txt", "w")
    if buscar_cedula+"\n" not in directorio:
        principal()
    else:
        
        for linea in directorio:
        
            if linea == buscar_cedula+"\n":
                
                indice = directorio.index(linea)
                directorio.pop(indice+1)
                directorio.pop(indice)
                directorio.pop(indice-1)
                
                agenda = open("agenda.txt", "w")
                for linea in directorio:
                    agenda.write(str(linea.strip()+"\n"))
                agenda.close()
                print("El usuario ha sido eliminado del listado")
        principal()

def buscar_lista(buscar_letra):
    directorio=[]
    lo_encontro=False
    try:
        agenda = open("agenda.txt", "r")
        directorio = agenda.readlines()
        agenda.close()
    except:
        agenda = open("agenda.txt", "w")
    
    print("Lista filtrada de beneficiarios:")
    for linea in directorio:
        if linea.startswith(buscar_letra)==True:
            lo_encontro=True
            indice = directorio.index(linea)
            print (directorio[indice].strip("\n"))
            print (directorio[indice+1].strip("\n"))
            print (directorio[indice+2].strip("\n"))
    principal()



principal ()

