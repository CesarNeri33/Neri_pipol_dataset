#!/usr/bin/env python
# coding: utf-8

# In[2]:


"""
Archivo: lambda_Expls.py
Descripción: Ejemplos prácticos de funciones lambda en Python.
Alumno: César Alejandro Neri Orozco
"""

def ejecutar_ejemplos():
    print("--- 1. Eliminación de Vocales ---")
    cadena_1 = "Python es super divertido"
    # Filtramos: solo pasan los caracteres que NO están en la cadena de vocales
    resultado_1 = "".join(filter(lambda c: c.lower() not in 'aeiouáéíóú', cadena_1))
    print(f"Original: {cadena_1}")
    print(f"Sin vocales: {resultado_1}\n")

    print("--- 2. Conteo de Caracteres ---")
    cadena_2 = "Hello World Hola Mundo"
    # Definimos la lambda y la ejecutamos inmediatamente
    conteo = (lambda s: len(s))(cadena_2)
    print(f"Cadena: {cadena_2}")
    print(f"Total caracteres: {conteo}\n")

    print("--- 3. Validación de Traslación (Rotación Circular) ---")
    # Ejemplo en el que los caracteres son los mismos pero han sido desplazados de su posición original.
    base = "abcdef"
    prueba = "cdefab"  # Ejemplo de la cadena "trasladada" o movida
    
    # Lógica: Si duplicamos la cadena base (s1 + s1), cualquier traslación 
    # posible de s1 debe estar contenida dentro del resultado.
    es_traslacion = lambda s1, s2: len(s1) == len(s2) and s1 in (s2 + s2)
    
    print(f"Cadena base: {base}")
    print(f"Cadena a validar: {prueba}")
    print(f"¿Es una traslación válida?: {es_traslacion(base, prueba)}")

if __name__ == "__main__":
    ejecutar_ejemplos()
