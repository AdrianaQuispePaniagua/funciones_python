import time
import funciones as fn

lista_alumnos = []
lista_notas = []

bandera_ejecucion_incorrecta = True
while bandera_ejecucion_incorrecta:
    print("=== APLICACION DE REGISTRO Y NOTAS DE ALUMNOS  ===")
    print("1. Agregar Alumno y notas")
    print("2. Mostrar Alumnos")
    print("3. Mostrar notas de un Alumno")
    print("4. Mostrar promedio de notas por control")
    print("5. Mostrar nota máxima y minima")
    print("6. Salir")
    print("Para ingresar al menú debe elegir e ingresar números enteros del 1 al 5. Gracias ")
    try:
        print("-----------------------------------------------------------------------------")
        opcion = int(input("Ingrese el número de la opción del menú que desea seleccionar: "))
        if opcion == 1:
            #validar nombre 
            bandera_nombre_incorrecto = True
            while bandera_nombre_incorrecto:
                nombre_alumno = input("ingrese el nombre del alumno: ").strip()
                if len(nombre_alumno) > 0:
                    bandera_nombre_incorrecto = False
                else:
                    print("El nombre de alumno no puede estar vacío")
            lista_alumnos.append(nombre_alumno)
            fn.agregar_notas(lista_notas)
            print("------------------------------------------------------------------------")           
        elif opcion == 2:
            print("------------------------------------------------------------------------")
            for i, alumno in enumerate(lista_alumnos):
                print(f"{i} - {alumno}")            
        elif opcion == 3:
            print("------------------------------------------------------------------------")
            for i, alumno in enumerate(lista_alumnos):
                print(f"{i} - {alumno}")
            indice = int(input("ingrese el indice del alumno para ver sus notas: "))
            fn.mostrar_notas(lista_alumnos, indice, lista_notas)
        elif opcion == 4:
            print("------------------------------------------------------------------------")
            fn.calcular_promedio(lista_alumnos, lista_notas)
        elif opcion == 5:
            print("------------------------------------------------------------------------")
            fn.mostrar_max_min(lista_notas)
        elif opcion == 6:
            print("------------------------------------------------------------------------")
            bandera_ejecucion_incorrecta = False
            print("Gracias por utilizar la aplicación.¡Hasta pronto!")
    except Exception:
        print("Opción inválida. Intente nuevamente..")
time.sleep(2)