"""
Tarea numero #1
Registro de Bitacoras
Angela Aguilar y Diego Araya
"""



"""
Nombre: bitacora
Entrada: Opcion de preferencia
Salida: Funcion correspondiente a la opcion elegida 
Restricciones: La opcion debe ser un valor numerico, de 1 a 5
"""
def bitacora():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Bienvenid@ al Registro de la Bitacora")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("Opciones:")
    print()
    print("(1) Registro de actividades")
    print()
    print("(2) Busquedas")
    print()
    print("(3) Cantidad de mensajes ")
    print()
    print("(4) Guardar mensajes")
    print()
    print("(5) Salir")
    print()

    opcion = input("Digite una opcion para continuar: ")



    if (opcion != ""):
        try:
            opcion= int(opcion)
        except:
            return" Error: El valor de la opcion debe ser numerico"    
        else:
            if opcion==1:
                return registro_de_Actividades()
            elif opcion==2:
                return busquedas()
            elif opcion == 3:
                return cantidad_Mensajes()
            elif opcion == 4:
                return guardar_Mensajes()
            elif opcion == 5:
                return salir()
            else:
                print( "Digite una opcion valida")
                return bitacora()
    else:
         return "Error digite un valor entre 1 y 5"
#--------------------------------------------------------------------------------------
"""
Nombre: Registro de actividades
Entrada: Opcion de preferencia
Salida: Funcion correspondiente a la opcion elegida 
Restricciones: La opcion debe ser un valor numerico, de 11 a 15
"""

def registro_de_Actividades():

     print()
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print("Registro de actividades")
     print("~~~~~~~~~~~~~~~~~~~~~~~")
     print()
     print("Opciones:")
     print()
     print("(11) Registro de  actividades")
     print()
     print("(12) Borrar actividad")
     print()
     print("(13) Modificar actividad")
     print()
     print("(14) Ver todas las actividades ")
     print()
     print("(15) Retornar")
     print()

     opcion= input("Seleccione una opcion: ")

     if (opcion != ""):
        try:
            opcion= int(opcion)
        except:
            return" Error: El valor de la opcion debe ser numerico"    
        else:
            if opcion== 11:
                return registrarActividad()
            elif opcion== 12:
                return borrarActividad()
            elif opcion == 13:
                return modificarActividad()
            elif opcion == 14:
                return verActividades()
            elif opcion == 15:
                return bitacora()
            else:
                return "Digite una opcion valida"
     else:
         return "Error digite un valor entre 11 y 15"
     

"""
Nombre: Registrar actividad
Entrada: Códio, Fecha,Hora,Usuario,Aplicación,Mensaje. 
Restricciones: Formato numérico
Fecha en formato DD/MM/YYYY
Formato HH:MM:SS AM/PM
Tamaño máximo del texto, 8 caracteres
Tamaño máximo del texto, 16 caracteres
Tamaño máximo del texto, 50 caracteres
"""




def registrarActividad():

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Registrar codigo automatico
  
    codigo= code()
    codigo= str(codigo)
    
    archivo = open("Bitacora.txt", encoding="utf-8",mode = "a")
    archivo.write(codigo)
    archivo.write(",")
    archivo.close()
              

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ingresar valor de fecha actual 

    import datetime
    fecha = datetime.date.today()
    fechaA = fecha.strftime("%d/%m/%Y")

    archivo = open("Bitacora.txt", encoding="utf-8",mode = "a")
    archivo.write(str(fechaA))
    archivo.write(",")
    archivo.close()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ingresar el valor de  la hora actual 
    
    hora = datetime.datetime.now().time()
    horaA = hora.strftime("%I:%M:%S %p")

    archivo = open("Bitacora.txt", encoding="utf-8",mode = "a")
    archivo.write(str(horaA))
    archivo.write(",")
    archivo.close()

    
#~~~~~~~~~~~~~~~~~~~~~~~~
#USUARIO
    print()
    usuario = input("Ingrese su usario: ")
    largoU= contarDigitos(usuario)
    if(usuario != ""):
        if largoU < 8:
            
            archivo = open("Bitacora.txt", encoding="utf-8",mode = "a")
            archivo.write(usuario)
            archivo.write(",")
            archivo.close()
        else:
            return "Error: el usuario debe tener como maximo 8 caracteres"
    else:
        return "Error: el usuario no debe ser vacio"
#APLICACION
    print()
    aplicacion = input("Ingrese la aplicacion: ")
    largoA= contarDigitos(aplicacion)
    if(aplicacion != ""):
        if largoA < 16:

            archivo = open("Bitacora.txt", encoding="utf-8",mode = "a")
            archivo.write(aplicacion)
            archivo.write(",")
            archivo.close()
        else:
            return "Error: la aplicacion debe tener como maximo 16 caracteres"   
    else:
        print("Error: la aplicacion no debe ser vacia")    

#MENSAJE
    print()
    mensaje = input("Ingrese su mensaje: ")
    largoM= contarDigitos(mensaje)
    if(mensaje != ""):
        if largoM < 50:
            
            archivo = open("Bitacora.txt", encoding="utf-8",mode = "a")
            archivo.write(mensaje)
            archivo.write("\n")
            archivo.close()
            print()
            print("El codigo para su actividad es: ",codigo)
            print("Su actividad fue registrada el dia ",fechaA,"a las ",horaA)
            return registro_de_Actividades()

            
        else:
            return "Error: el mensaje debe tener como maximo 50 caracteres"    
    else:
        print("Error: el mensaje no debe ser vacio")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Codigos utiles para registrar actividad

#codigo automoatico 
def code():
    codigoNuevo=0

    archivo= open("Bitacora.txt",encoding="utf-8",mode = "r")
    lineas=archivo.readlines()
    archivo.close

    ultimaLinea= lineas[-1]
    
    lista= ultimaLinea.split(",")

    codigoI=int(lista[0])

    codigoNuevo+= codigoI + 1

    return codigoNuevo
    

#contardigitos texto

def contarDigitos(x):
    contador=0

    for i in x:
      contador+=1

    return contador  
        
    
        
"""
Nombre: Borrar actividad
Entrada: Codigo
Restricciones: Código válido, existente en el documento,
de no existir, mostrar el mensaje
respectivo al usuario 

"""
def borrarActividad():
    print("estas en borrar actividad")
    return registro_de_Actividades()

    
    


"""
Nombre: Modificar actividad
Entrada: Código: Existente y válido, Fecha,Hora,Usuario,Aplicación,Mensaje.
Restricciones:Formato numérico
Fecha en formato DD/MM/YYYY
Formato HH:MM:SS AM/PM
Tamaño máximo del texto, 8 caracteres
Tamaño máximo del texto, 16 caracteres
Tamaño máximo del texto, 50 caracteres 

"""     

def modificarActividad():
    print("estas en modificar")
    return registro_de_Actividades()


    
"""
Nombre: Ver actividades 
Salida: Todos los contactos registrados 
"""  
def verActividades():
    print("estas en ver actividades")
    return registro_de_Actividades()


#-------------------------------------------------------------------------------------    

"""
Nombre: Busquedas
Entrada: opcion de preferencia
Salida: Funcion correspondiente a la elegida
Restricciones: 
La opcion debe ser un valor numerico, de 21 a 24
"""

def busquedas():

     print()
     print("~~~~~~~~~~~~")
     print("Busquedas")
     print("~~~~~~~~~~~")
     print()
     print("Opciones:")
     print()
     print("(21) Buscar por usuario")
     print()
     print("(22) Buscar por aplicacion")
     print()
     print("(23) Buscar por fecha")
     print()
     print("(24) Retornar ")
     print()


     opcion= input("Seleccione una opcion: ")

     if (opcion != ""):
        try:
            opcion= int(opcion)
        except:
            return" Error: El valor de la opcion debe ser numerico"    
        else:
            if opcion== 21:
                return buscarUsuario()
            elif opcion== 22:
                return buscarAplicacion()
            elif opcion == 23:
                return buscarFecha()
            elif opcion == 24:
                return bitacora()
            else:
                return "Digite una opcion valida"
     else:
         return "Error digite un valor entre 11 y 15"
     

"""
Nombre: Buscar por usuario 
Entrada: Parte del nombre del usuario

Salida: Actividad correspondiente
Restricciones: No debe permitir valores en blanco o nulos 
""" 

def buscarUsuario():

    usuario= input("Ingrese su usario: ")

    archivo= open("Bitacora.txt",encoding="utf-8",mode = "r")
    lineas=archivo.readlines()
    archivo.close
    

    

    ultimaLinea= lineas[-1]
    
    lista= ultimaLinea.split(",")

    
    return lista



    
    #return busquedas()



"""
Nombre: Buscar por aplicacion 
Entrada: Parte del nombre de la aplicacion
Salida: Actividad correspondiente
Restricciones: No debe permitir valores en blanco o nulos 
""" 

def buscarAplicacion():
    print("estas en buscar aplicacion")
    return busquedas()

"""
Nombre: Buscar por Fecha 
Entrada:Rango de fechas, inicio y final 
Salida: Actividad correspondiente
Restricciones: No debe permitir valores en blanco o nulos 
""" 

def buscarFecha():
    print("estas en buscar fecha")
    return busquedas()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Nombre: Cantidad de mensajes
Salida: Devuelve  el total de contactos almacenados 
"""
def cantidad_Mensajes():
    print("estas en cantidad menajes")
    return busquedas()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Nombre: Guardar mensajes  
Entrada: Rango de fechas, inicio y final y Nombre de archivo 
Salida:Extrae los mensajes dentro del rango de
fechas y los guarda en otro archivo.
Restricciones: Formato de fechas válidas, El nombre del archivo no debe ser vacío 

""" 
def guardar_Mensajes():
    print("estas en guardar mensaje")
    return busquedas()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def salir():
    return "Gracias por usar la bitacora"






def registrar():
    import datetime
    fecha = datetime.datetime.now()

    archivo = open("Bitacora.txt", encoding="utf-8",mode = "a")
    archivo.write(str(fecha))
    archivo.close()
            



def prueba():
    codigo=0
    while codigo == codigo:
        codigo+=1
    print(codigo)    

