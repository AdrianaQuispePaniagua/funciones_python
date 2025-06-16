def agregar_notas(lista_notas):
    for i in range(3):
        #validar notas alumnos
        bandera_nota_alumno_incorrecto = True
        while bandera_nota_alumno_incorrecto:
            try:
                notas_alumno = float(input(f"Ingrese la nota {i + 1} del alumno del 0 al 7: "))
                if notas_alumno > 0:
                    bandera_nota_alumno_incorrecto = False
                else:
                    print("Ingrese valores númericos y mayores o iguales a 0")
            except Exception:
                print("Debe ingresar valores númericos positivos")
        lista_notas.append(notas_alumno)

def mostrar_notas(lista_alumnos, indice, lista_notas):
    print(f"las notas del alumno {lista_alumnos[indice]} son:")
    indice_primera_nota = indice * 3
    print(f" nota 1: {lista_notas[indice_primera_nota]}")
    print(f" nota 2: {lista_notas[indice_primera_nota + 1]}")
    print(f" nota 3: {lista_notas[indice_primera_nota + 2]}")

def calcular_promedio(lista_alumnos, lista_notas):
    suma_control_1 = 0
    suma_control_2 = 0
    suma_control_3 = 0
    for i in range(len(lista_alumnos)):
        indice_primera_nota = i * 3
        suma_control_1 = suma_control_1 + lista_notas[indice_primera_nota]
        suma_control_2 = suma_control_2 + lista_notas[indice_primera_nota + 1]
        suma_control_3 = suma_control_3 + lista_notas[indice_primera_nota + 2]
            
    promedio_control_1 = suma_control_1 / len(lista_alumnos)
    promedio_control_2 = suma_control_2 / len(lista_alumnos)
    promedio_control_3 = suma_control_3 / len(lista_alumnos)
    print(f"El promedio del primer control es: {promedio_control_1: .2f}")
    print(f"El promedio del segundo control es: {promedio_control_2: .2f}")
    print(f"El promedio del tercer control es: {promedio_control_3: .2f}")

def mostrar_max_min(lista_notas):
    mayor = -1
    menor = 8
    for x in lista_notas:
        if x > mayor:
            mayor = x
        if x < menor:
            menor = x
    print(f"la nota maxima es: {mayor}")
    print(f"la nota minima es: {menor}")
       