def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = 4
resultado = es_primo(numero)
print("¿Es primo el número?", resultado)
