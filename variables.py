import sys
import subprocess

# Verificar si la librería keyboard está instalada
try:
    import keyboard
except ImportError:
    print("La librería 'keyboard' no está instalada.")
    print("Instalando automáticamente...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keyboard"])
    import keyboard


def main():
    x = -5
    y = 3
    pi = 3.1416
    e = 2.7182

    print(x, y)
    print("Qué número desea mostrar???")
    print("E = Enteros")
    print("F = Flotantes")
    print("D = Capturar Datos Personales")

    while True:

        if keyboard.is_pressed('e'):
            print("\n¡Tecla 'E' presionada!")
            print("Enteros:", x, y)
            break

        if keyboard.is_pressed('f'):
            print("\n¡Tecla 'F' presionada!")
            print("Flotantes:", pi, e)
            break

        if keyboard.is_pressed('d'):
            print("\n¡Tecla 'D' presionada!")
            print("=== Captura de Datos ===")

            nombre = input("Ingresa tu nombre: ")
            apellido = input("Ingresa tu apellido: ")
            estatura = input("Ingresa tu estatura (ejemplo 1.75): ")

            # Validar que edad sea numérica
            while True:
                try:
                    edad = int(input("Ingresa tu edad: "))
                    break
                except ValueError:
                    print("Error: La edad debe ser un número entero.")

            print("\n=== Datos Capturados ===")
            print("Nombre completo:", nombre, apellido)
            print("Estatura:", estatura)
            print("Edad:", edad)

            if edad >= 18:
                print("Eres mayor de edad.")
            else:
                print("Eres menor de edad.")

            break


if __name__ == "__main__":
    main()