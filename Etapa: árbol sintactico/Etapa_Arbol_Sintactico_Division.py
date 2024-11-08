def dividir(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError:
        resultado = "Error: División entre cero"
    return resultado

print("Resultado de 10 / 2:", dividir(10, 2))
print("Resultado de 10 / 5:", dividir(10, 5))
