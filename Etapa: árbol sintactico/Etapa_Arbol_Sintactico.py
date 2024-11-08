# Variable global
a = 0

# Definición de la función suma
def suma(a, b):
    return a + b

# Función principal
def main():
    # Variables locales
    a = 0.0  # variable local 'a' (enmascara la global)
    b = 0
    c = 0
    
    # Operación de suma y asignación
    c = a + b  # Suma de 'a' (float) y 'b' (int)
    print("Resultado de c = a + b:", c)
    
    # Llamada a la función suma
    c = suma(8, 9)
    print("Resultado de c = suma(8, 9):", c)

# Llamada a la función principal
if __name__ == "__main__":
    main()
