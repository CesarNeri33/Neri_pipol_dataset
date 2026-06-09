# César Alejandro Neri Orozco
# Operaciones con Arrays usando NumPy

import numpy as np

vector = None
matriz = None

while True:

    print("\n========= MENU =========")
    print("1) Crear vector")
    print("2) Crear matriz")
    print("3) Operaciones básicas")
    print("4) Operaciones especiales")
    print("5) Crear matriz de ceros")
    print("6) Crear matriz de unos")
    print("7) Crear matriz identidad")
    print("0) Salir")

    opcion = input("Seleccione una opción: ")

    # 1 Crear vector
    if opcion == "1":
        n = int(input("Cantidad de elementos del vector: "))
        datos = []

        for i in range(n):
            valor = float(input(f"Ingrese elemento {i+1}: "))
            datos.append(valor)

        vector = np.array(datos)
        print("Vector creado:", vector)

    # 2 Crear matriz
    elif opcion == "2":
        filas = int(input("Número de renglones: "))
        columnas = int(input("Número de columnas: "))

        datos = []

        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = float(input(f"Elemento [{i}][{j}]: "))
                fila.append(valor)
            datos.append(fila)

        matriz = np.array(datos)
        print("Matriz creada:")
        print(matriz)

    # 3 Operaciones básicas
    elif opcion == "3":

        print("\nOperaciones:")
        print("1) Suma")
        print("2) Resta")
        print("3) Multiplicación")
        print("4) División entera")

        op = input("Seleccione operación: ")
        num = float(input("Ingrese el número para operar: "))

        if vector is not None:

            if op == "1":
                print("Resultado:", vector + num)

            elif op == "2":
                print("Resultado:", vector - num)

            elif op == "3":
                print("Resultado:", vector * num)

            elif op == "4":
                print("Resultado:", vector // num)

        elif matriz is not None:

            if op == "1":
                print("Resultado:\n", matriz + num)

            elif op == "2":
                print("Resultado:\n", matriz - num)

            elif op == "3":
                print("Resultado:\n", matriz * num)

            elif op == "4":
                print("Resultado:\n", matriz // num)

        else:
            print("Primero debe crear un vector o matriz.")

    # 4 Operaciones especiales
    elif opcion == "4":

        print("\nOperaciones especiales:")
        print("1) Multiplicar por PI")
        print("2) Seno")
        print("3) Coseno")
        print("4) Logaritmo natural")

        op = input("Seleccione operación: ")

        if vector is not None:

            if op == "1":
                print(vector * np.pi)

            elif op == "2":
                print(np.sin(vector))

            elif op == "3":
                print(np.cos(vector))

            elif op == "4":
                print(np.log(vector))

        elif matriz is not None:

            if op == "1":
                print(matriz * np.pi)

            elif op == "2":
                print(np.sin(matriz))

            elif op == "3":
                print(np.cos(matriz))

            elif op == "4":
                print(np.log(matriz))

        else:
            print("Primero cree un vector o matriz.")

    # 5 Matriz de ceros
    elif opcion == "5":

        filas = int(input("Filas: "))
        columnas = int(input("Columnas: "))

        matriz = np.zeros((filas, columnas))

        print("Matriz de ceros:")
        print(matriz)

    # 6 Matriz de unos
    elif opcion == "6":

        filas = int(input("Filas: "))
        columnas = int(input("Columnas: "))

        matriz = np.ones((filas, columnas))

        print("Matriz de unos:")
        print(matriz)

    # 7 Matriz identidad
    elif opcion == "7":

        n = int(input("Tamaño de la matriz identidad: "))

        matriz = np.identity(n)

        print("Matriz identidad:")
        print(matriz)

    # Salir
    elif opcion == "0":
        print("Programa terminado.")
        break

    else:
        print("Opción no válida.")