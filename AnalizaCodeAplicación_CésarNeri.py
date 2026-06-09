import sys

# 1.- Definicion de la funcion
# Verifica: mismos caracteres y que s_2 esté en la duplicación de s_1.
are_rotations = lambda s_1, s_2: sorted(s_1) == sorted(s_2) and s_2 in s_1 + s_1

def validar_cadena(cadena, nombre):
    """Valida que la cadena sea alfabética, sin espacios y no esté vacía."""
    if not cadena:
        return False, f"Error: La {nombre} no puede estar vacía."
    if not cadena.isalpha():
        return False, f"Error: La {nombre} debe contener solo caracteres alfabéticos (sin espacios ni números)."
    return True, ""

def ejecutar_programa():
    print("--- Verificador de Rotación de Cadenas ---")
    
    # Entrada de datos
    str1 = input("Introduce la primera cadena: ")
    str2 = input("Introduce la segunda cadena: ")

    # 2. Validaciones
    # Validar caracteres alfabéticos y sin espacios
    val1, msg1 = validar_cadena(str1, "primera cadena")
    val2, msg2 = validar_cadena(str2, "segunda cadena")

    if not val1:
        print(msg1)
        return
    if not val2:
        print(msg2)
        return

    # Validar longitud (si no miden lo mismo, no pueden ser rotaciones)
    if len(str1) != len(str2):
        print(f"\nResultado: NO se cumple la traslación.")
        print("Razón: Las cadenas tienen longitudes diferentes.")
        return

    # 3. Aplicación de la lógica
    # Python diferencia mayúsculas de minúsculas por defecto ('A' != 'a')
    es_rotacion = are_rotations(str1, str2)

    # 4. Mensaje de resultado
    print("\n" + "="*40)
    if es_rotacion:
        print(f"¡ÉXITO! La cadena '{str2}' es una rotación de '{str1}'.")
        print("Estado: Se cumple la traslación perfectamente.")
    else:
        print(f"FALLO: La cadena '{str2}' NO es una rotación de '{str1}'.")
        print("Estado: No se cumple la traslación.")
    print("="*40)

if __name__ == "__main__":
    ejecutar_programa()
