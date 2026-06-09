import numpy as np

# ---------------------------
# Función para ingresar matriz manualmente
# ---------------------------
def matriz_manual():
    n = int(input("Ingrese el tamaño de la matriz cuadrada (n): "))
    matriz = []

    print("Ingrese los valores fila por fila:")

    for i in range(n):
        fila = []
        for j in range(n):
            valor = float(input(f"Elemento [{i+1},{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)

    return np.array(matriz)


# ---------------------------
# Función para generar matriz automática
# ---------------------------
def matriz_automatica():
    n = int(input("Ingrese el tamaño de la matriz cuadrada (n): "))
    matriz = np.random.randint(1, 10, (n, n))
    print("\nMatriz generada automáticamente:")
    print(matriz)
    return matriz


# ---------------------------
# Selección de tipo de matriz
# ---------------------------
def obtener_matriz():
    print("\nSeleccione cómo desea obtener la matriz:")
    print("1. Ingresar matriz manualmente")
    print("2. Generar matriz automáticamente")

    opcion = input("Opción: ")

    if opcion == "1":
        return matriz_manual()
    elif opcion == "2":
        return matriz_automatica()
    else:
        print("Opción inválida.")
        return None


# ---------------------------
# Menú principal
# ---------------------------
def menu():
    while True:
        print("\n====== MENÚ ======")
        print("1. Calcular Eigenvalores")
        print("2. Calcular Eigenvectores")
        print("3. Calcular Eigenvalores y Eigenvectores")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "4":
            print("Programa finalizado.")
            break

        matriz = obtener_matriz()

        if matriz is None:
            continue

        # Cálculo
        valores, vectores = np.linalg.eig(matriz)

        if opcion == "1":
            print("\nEigenvalores:")
            print(valores)

        elif opcion == "2":
            print("\nEigenvectores:")
            print(vectores)

        elif opcion == "3":
            print("\nEigenvalores:")
            print(valores)
            print("\nEigenvectores:")
            print(vectores)

        else:
            print("Opción inválida.")


# Ejecutar programa
menu()