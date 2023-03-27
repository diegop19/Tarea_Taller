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
                print( "Digite un valor entre uno y cinco")
                return bitacora()
    else:
         print ("Digite una opcion valida")
         return bitacora()
        
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
     print("(11) Registrar actividad")
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
                print( "Digite una opcion valida")
                return registro_de_Actividades()
     else:
         print( "Error digite un valor entre 11 y 15")
         return registro_de_Actividades()
     

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
    
    archivo = open("Bitácora.txt", encoding="utf-8",mode = "a")
    archivo.write(codigo)
    archivo.write(",")
    archivo.close()
              

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ingresar valor de fecha actual 

    import datetime
    fecha = datetime.date.today()
    fechaA = fecha.strftime("%d/%m/%Y")

    archivo = open("Bitácora.txt", encoding="utf-8",mode = "a")
    archivo.write(str(fechaA))
    archivo.write(",")
    archivo.close()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ingresar el valor de  la hora actual 
    
    hora = datetime.datetime.now().time()
    horaA = hora.strftime("%I:%M:%S %p")

    archivo = open("Bitácora.txt", encoding="utf-8",mode = "a")
    archivo.write(str(horaA))
    archivo.write(",")
    archivo.close()

    
#~~~~~~~~~~~~~~~~~~~~~~~~
#USUARIO
    print()
    usuario = input("Ingrese su usario: ")
    largoU= contarDigitos(usuario)
    if(usuario != ""):
        if largoU <= 8:
            
            archivo = open("Bitácora.txt", encoding="utf-8",mode = "a")
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
        if largoA <= 16:

            archivo = open("Bitácora.txt", encoding="utf-8",mode = "a")
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
        if largoM <= 50:
            
            archivo = open("Bitácora.txt", encoding="utf-8",mode = "a")
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

    archivo= open("Bitácora.txt",encoding="utf-8",mode = "r")
    lineas=archivo.readlines()
    archivo.close

    
    if lineas != []:
        
        ultimaLinea= lineas[-1]
        lista= ultimaLinea.split(",")

        codigoI=int(lista[0])

        codigoNuevo+= codigoI + 1
        
    else:
        codigoNuevo+=1
    return codigoNuevo
    

#contardigitos texto

def contarDigitos(x):
    contador=0

    for i in x:
      contador+=1

    return contador  
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
        
"""
Nombre: Borrar actividad
Entrada: Codigo
Restricciones: Código válido, existente en el documento,
de no existir, mostrar el mensaje
respectivo al usuario 

"""
def borrarActividad():
    print()
    codigo= input("Ingrese el codigo de la actividad que desea borrar: ")

    if codigo != "":
    
        archivo = open("Bitácora.txt", encoding="utf-8", mode="r")
        lineas = archivo.readlines()
        archivo.close()
        
        archivo = open("Bitácora.txt", encoding="utf-8", mode="w")

        for linea in lineas:
            contenido = linea.strip().split(",")
            registro = contenido[0]
            if codigo != registro:
                archivo.write(linea)
        archivo.close()
        
        print("La actividad con código", codigo, "ha sido borrada exitosamente.")
    else:
          print("Error: el código de la actividad no debe ser vacío.")

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
     
    codigo= input("Ingrese el codigo de la actividad que desea modificar: ")

    if codigo != "":
    
        archivo = open("Bitácora.txt", encoding="utf-8", mode="r")
        lineas = archivo.readlines()
        archivo.close()

        modificar = registrarV2()
        modificar = str(modificar)
        
        archivo = open("Bitácora.txt", encoding="utf-8", mode="w")
        
        for linea in lineas:
            contenido = linea.strip().split(",")
            registro = contenido[0]
            if codigo != registro:
                archivo.write(linea)
            else:
                 archivo.write(codigo)
                 archivo.write(",")
                 archivo.write(modificar)
                 archivo.write("\n")
        archivo.close()
        
        print("La actividad con código", codigo, "ha sido modificada exitosamente.")
    else:
          print("Error: el código de la actividad no debe ser vacío.")

    return registro_de_Actividades()



def registrarV2():
    
    import datetime
    fecha = datetime.date.today()
    fechaA = fecha.strftime("%d/%m/%Y")
    

  
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Ingresar el valor de  la hora actual 
    
    hora = datetime.datetime.now().time()
    horaA = hora.strftime("%I:%M:%S %p")
    


#~~~~~~~~~~~~~~~~~~~~~~~~
#USUARIO
    print()
    usuario = input("Ingrese el usuario que desea modificar : ")
    largoU= contarDigitos(usuario)
    if(usuario != ""):
        if largoU <= 8:
            None
        else:
            return "Error: el usuario debe tener como maximo 8 caracteres"
    else:
        return "Error: el usuario no debe ser vacio"
#APLICACION
    print()
    aplicacion = input("Ingrese la aplicacion que desea modificar: ")
    largoA= contarDigitos(aplicacion)
    if(aplicacion != ""):
        if largoA <= 16:
            None

        else:
            return "Error: la aplicacion debe tener como maximo 16 caracteres"   
    else:
        print("Error: la aplicacion no debe ser vacia")    

#MENSAJE
    print()
    mensaje = input("Ingrese el mensaje que desea modificar : ")
    largoM= contarDigitos(mensaje)
    if(mensaje != ""):
        if largoM <= 50:
    
            return fechaA + ',' + horaA + ',' + usuario + ',' + aplicacion + ',' + mensaje
            
        else:
            return "Error: el mensaje debe tener como maximo 50 caracteres"    
    else:
        print("Error: el mensaje no debe ser vacio")

    
"""
Nombre: Ver actividades 
Salida: Todos los contactos registrados 
"""  
def verActividades():
    print()
    print("Actividades registradas : ")
    print()

    archivo = open("Bitácora.txt", encoding="utf-8",mode = "r")
    lineas = archivo.readlines()
    archivo.close()

    for linea in lineas:
        if linea != "":
           print(linea)
       
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
         return "Error digite un valor entre 21 y 24"
     

"""
Nombre: Buscar por usuario 
Entrada: Parte del nombre del usuario

Salida: Actividad correspondiente
Restricciones: No debe permitir valores en blanco o nulos 
""" 

def buscarUsuario():
    print()
    usuario= input("Ingrese su usuario: ")
    print()
    coincidencia = False
    if usuario != "":
        
       archivo = open("Bitácora.txt", encoding="utf-8",mode = "r")
       lineas = archivo.readlines()
       archivo.close()

       for linea in lineas:

           contenido = linea.strip().split(",")
           registro= contenido[3]

           if usuario == registro:
               coincidencia=True
               #print("La coicidencia encontrada es: ")
               print(linea)
            
           else:
               continue
       if coincidencia == True:
           print("Estas fueron la o las coincidencias encontradas ^ ")
       else:
           print("Error: no hay coincidencias en el usuario, verifique que este escrito correctamente")
            
    else:
        print("Error: el usuario no debe ser vacio")
        

"""
Nombre: Buscar por aplicacion 
Entrada: Parte del nombre de la aplicacion
Salida: Actividad correspondiente
Restricciones: No debe permitir valores en blanco o nulos 
""" 

def buscarAplicacion():
    print()
    aplicacion= input("Ingrese el nombre de la aplicaion a buscar:  ")
    print()
    coincidencia = False
    if aplicacion != "":
        
       archivo = open("Bitácora.txt", encoding="utf-8",mode = "r")
       lineas = archivo.readlines()
       archivo.close()

       for linea in lineas:

           contenido = linea.strip().split(",")
           registro= contenido[4]

           if aplicacion == registro:
               coincidencia=True
               print(linea)
            
           else:
               continue
       if coincidencia == True:
           print("Estas fueron la o las coincidencias encontradas ^ ")
       else:
           print("Error: no hay coincidencias en el nombre de la aplicacion, verifique que este escrito correctamente")
            
    else:
        print("Error: la aplicacion no debe ser vacia")
        

"""
Nombre: Buscar por Fecha 
Entrada:Rango de fechas, inicio y final 
Salida: Actividad correspondiente
Restricciones: No debe permitir valores en blanco o nulos 
""" 

def buscarFecha():
    print()
    print("La busqueda de fechas se realiza por rangos, ingrese las fechas entre las cuales quiere buscar actividades")
    print("recuerde que el formato de fechas debe ser DD/MM/YY")
    print()
    
    inicio= input("Ingrese el inicio : ")
    final= input("Ingrese el final : ")

    if inicio != "" and final != "":
        archivo = open("Bitácora.txt", encoding="utf-8", mode="r")
        lineas = archivo.readlines()
        archivo.close()

        actividades = []

        for linea in lineas:
            contenido = linea.strip().split(",")
            registro = contenido[1]
            print(linea[-1])

            if inicio <= registro <= final:
                actividades += [linea]
                
        if actividades:
            for actividad in actividades:
                print(actividad)
        else:   
           print("No se encontraron actividades en el rango de fechas especificado.")
            
    else:
        print("Error: los valores de inicio y final no deben ser vacios")
        return buscarfecha()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
Nombre: Cantidad de mensajes
Salida: Devuelve  el total de contactos almacenados 
"""
def cantidad_Mensajes():
     contador=0 

     archivo = open("Bitácora.txt", encoding="utf-8",mode = "r")
     lineas = archivo.readlines()
     archivo.close()

     while lineas != []:
         contador+=1
         lineas= lineas[:-1]
        
     print()
     print("El total de sus contactos es : ", contador)
     print()
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
    print()
    print("~~~~~~~~~~~~~~~~~")
    print("Guardar Mensajes")
    print("~~~~~~~~~~~~~~~~~")
    print()
    print("+Para guardar mensajes debe ingresar el nombre del archivo en el que lo desea guardar.")
    print()
    print("+Recuerde que el formato del archivo debe ser .txt")
    print()
    
    nombreArchivo = input("Ingrese el nombre del archivo : ")
    inicio= input("Ingrese el inicio : ")
    final= input("Ingrese el final : ")
    print()

    if inicio != "" and final != "" and nombreArchivo != "":
        archivo = open("Bitácora.txt", encoding="utf-8", mode="r")
        lineas = archivo.readlines()
        archivo.close()
        coincidencias = False

        

        for linea in lineas:
            contenido = linea.strip().split(",")
            registro = contenido[1]
          
            

            if inicio <= registro <= final:
                coincidencias= True
                mensajes = contenido[-1]
                archivo2 = open(nombreArchivo,encoding="utf-8", mode="a")
                archivo2.write(mensajes)
                archivo2.write("\n")
                archivo.close()

        if coincidencias == True:
            print("Sus mensajes han sido guardados exitosamente :)")
            print()
            return bitacora()
                
        else:
            print("No se encontraron actividades en el rango de fechas especificado.")
            print()
            return guardar_Mensajes()
            
    else:
        print("Error: los valores de inicio, final o el nombre del archivo no deben ser vacios")
        

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def salir():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print( "Gracias por usar la bitacora")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    return 





            




