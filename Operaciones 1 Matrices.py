import numpy as np

# Crear matriz ingresada por el usuario
def crear_matriz():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    matriz = []

    print("Ingrese los valores de la matriz:")

    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Elemento [{i+1},{j+1}]: "))
            fila.append(valor)
        matriz.append(fila)

    return np.array(matriz)

# Menú de operaciones
def menu():
    print("\n----- MENÚ DE OPERACIONES -----")
    print("1. Determinante de la matriz")
    print("2. Inversa de la matriz")
    print("3. Eigenvalores y Eigenvectores")
    print("4. Rango de la matriz")
    print("5. Norma de la matriz")
    print("6. Salir")

def main():
    print("Programa de operaciones con matrices usando Numpy")

    matriz = crear_matriz()
    print("\nMatriz ingresada:")
    print(matriz)

    while True:
        menu()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            if matriz.shape[0] == matriz.shape[1]:
                det = np.linalg.det(matriz)
                print("Determinante:", det)
            else:
                print("El determinante solo existe para matrices cuadradas")

        elif opcion == 2:
            if matriz.shape[0] == matriz.shape[1]:
                try:
                    inv = np.linalg.inv(matriz)
                    print("Matriz inversa:")
                    print(inv)
                except:
                    print("La matriz no tiene inversa")
            else:
                print("La inversa solo existe para matrices cuadradas")

        elif opcion == 3:
            if matriz.shape[0] == matriz.shape[1]:
                valores, vectores = np.linalg.eig(matriz)
                print("Eigenvalores:")
                print(valores)
                print("Eigenvectores:")
                print(vectores)
            else:
                print("Los eigenvalores requieren matriz cuadrada")

        elif opcion == 4:
            rango = np.linalg.matrix_rank(matriz)
            print("Rango de la matriz:", rango)

        elif opcion == 5:
            norma = np.linalg.norm(matriz)
            print("Norma de la matriz:", norma)

        elif opcion == 6:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()