



bandera_de_ejecucion_incorrecta = True
while bandera_de_ejecucion_incorrecta:
    print("---APLICACION MINI AGENDA DE CONTACTOS--")
    print("1.Agregar un contacto: nombre, teléfono, email")
    print("2.Lista de contactos guardados") 
    print("3.Buscar un contacto por nombre")
    print("4.Eliminar un contacto")
    print("5.Salir del programa")
    print("Para ingresar al menu debe elegir o ingresar un número entero del 1 al 5. Gracias")
    try:
        opcion = int(input("Ingrese el número de la opción del menú que deseas seleccionar: "))
        if opcion == 1:
            print("Aqui agrega el contacto nombre, telefono y correo")
        elif opcion == 2:
            print("Mostrar contactos")
        elif opcion == 3:
            print("Busca contacto")
        elif opcion == 4:
            print("Elimina contacto")
        elif opcion == 5:
            bandera_de_ejecucion_incorrecta = False
            print("Gracias por utilizar la aplicación. Hasta pronto!")
    except:
        print("La opción ingresada es invalida. Intente nuevamente")