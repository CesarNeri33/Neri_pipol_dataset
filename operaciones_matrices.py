import numpy as np
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def generar_matriz(filas, columnas, modo):
    """Genera una matriz de forma manual o automática."""
    if modo == 1: # Manual
        print(f"\n--- Ingreso Manual ({filas}x{columnas}) ---")
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                val = float(input(f"Elemento [{i+1}][{j+1}]: "))
                fila.append(val)
            matriz.append(fila)
        return np.array(matriz)
    else: # Automática
        print(f"\n--- Generación Automática ({filas}x{columnas}) ---")
        return np.random.randint(1, 11, size=(filas, columnas)).astype(float)

def mostrar_menu():
    print("\n" + "="*30)
    print("   ÁLGEBRA LINEAL CON NUMPY")
    print("="*30)
    print("1. Suma de Matrices")
    print("2. Resta de Matrices")
    print("3. Multiplicación (Producto Punto)")
    print("4. Transpuesta de una Matriz")
    print("5. Multiplicación por Escalar")
    print("6. Salir")
    print("="*30)

def ejecutar_operacion():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Saliendo del programa...")
            break

        if opcion in ["1", "2", "3", "5"]:
            f1 = int(input("Filas de la Matriz A: "))
            c1 = int(input("Columnas de la Matriz A: "))
            
            modo = int(input("¿Cómo desea llenar la Matriz A? (1.Manual / 2.Automático): "))
            A = generar_matriz(f1, c1, modo)
            print("\nMatriz A:\n", A)

            if opcion in ["1", "2", "3"]:
                if opcion == "3":
                    f2 = int(input("Filas de la Matriz B (debe ser igual a col de A): "))
                    c2 = int(input("Columnas de la Matriz B: "))
                else:
                    f2, c2 = f1, c1
                
                modo2 = int(input("¿Cómo desea llenar la Matriz B? (1.Manual / 2.Automático): "))
                B = generar_matriz(f2, c2, modo2)
                print("\nMatriz B:\n", B)

            # --- Lógica de Operaciones ---
            try:
                if opcion == "1":
                    # SUMA: np.add(A, B) o A + B
                    resultado = A + B
                    print("\nResultado (A + B):\n", resultado)
                
                elif opcion == "2":
                    # RESTA: np.subtract(A, B) o A - B
                    resultado = A - B
                    print("\nResultado (A - B):\n", resultado)

                elif opcion == "3":
                    # PRODUCTO PUNTO: np.dot(A, B) o A @ B
                    resultado = A @ B
                    print("\nResultado (A @ B):\n", resultado)

                elif opcion == "5":
                    k = float(input("Ingrese el escalar: "))
                    # ESCALAR: np.multiply(k, A) o k * A
                    resultado = k * A
                    print(f"\nResultado ({k} * A):\n", resultado)

            except ValueError as e:
                print("\n[ERROR]: Las dimensiones no son compatibles para esta operación.")
                print(e)

        elif opcion == "4":
            f = int(input("Filas: "))
            c = int(input("Columnas: "))
            modo = int(input("Llenado (1.Manual / 2.Automático): "))
            A = generar_matriz(f, c, modo)
            print("\nMatriz Original:\n", A)
            # TRANSPUESTA: A.T o np.transpose(A)
            print("\nMatriz Transpuesta:\n", A.T)

        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    ejecutar_operacion()