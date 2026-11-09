import math
import random

def punto_aleatorio(a, b):
    x = a * (2 * random.random() - 1)
    y = b * (2 * random.random() - 1)
    return x, y

def en_elipse(x, y, a, b):
    return (x * x) / (a * a) + (y * y) / (b * b) <= 1

def en_hiperbola(x, y, c, d):
    return (x * x) / (c * c) - (y * y) / (d * d) >= 1

def leer_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            print("  Debe ser un número positivo.")
        except ValueError:
            print("  Entrada inválida, escriba un número.")

def leer_entero_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("  Debe ser un entero positivo.")
        except ValueError:
            print("  Entrada inválida, escriba un número entero.")

def main():
    print("=== Área de intersección entre elipse e hipérbola (Monte Carlo) ===")

    a = leer_positivo("Ingrese el valor de a (semieje elipse): ")
    b = leer_positivo("Ingrese el valor de b (semieje elipse): ")
    c = leer_positivo("Ingrese el valor de c (hipérbola): ")
    d = leer_positivo("Ingrese el valor de d (hipérbola): ")
    n = leer_entero_positivo("Cantidad de números aleatorios: ")

    puntos_elipse = 0
    puntos_interseccion = 0

    for _ in range(n):
        x, y = punto_aleatorio(a, b)

        if en_elipse(x, y, a, b):
            puntos_elipse += 1
            if en_hiperbola(x, y, c, d):
                puntos_interseccion += 1

    area_elipse = math.pi * a * b

    print("\n--- Resultados ---")
    print(f"Puntos generados (en el rectángulo delimitador): {n}")
    print(f"Puntos que cayeron dentro de la elipse: {puntos_elipse}")
    print(f"Puntos que cayeron en la intersección: {puntos_interseccion}")

    if puntos_elipse == 0:
        print("Ningún punto cayó en la elipse; use una mayor cantidad de puntos.")
        return

    area_interseccion_mc = area_elipse * (puntos_interseccion / puntos_elipse)

    print(f"\nÁrea calculada de la elipse: {area_elipse:.4f}")
    print(f"Área aproximada de la intersección (Monte Carlo): {area_interseccion_mc:.4f}")

if __name__ == "__main__":
    main()