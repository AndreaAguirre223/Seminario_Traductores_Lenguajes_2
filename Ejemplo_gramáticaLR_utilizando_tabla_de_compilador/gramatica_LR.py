
import re

# ======================
# Tabla LR
# ======================
# Tabla de acciones (action)
action = {
    (0, 'Int'): ('shift', 5),
    (5, 'ID'): ('shift', 8),
    (8, ';'): ('reduce', 6),  # R6: DefVar ::= tipo identificador ListaVar ;
    (8, 'ListaVar'): ('reduce', 7),  # R7: ListaVar ::= ε
    (12, '$'): ('reduce', 6),  # R6: DefVar ::= tipo identificador ListaVar ;
    (4, 'DefVar'): ('reduce', 4),  # R4: Definicion ::= DefVar
    (3, 'Definicion'): ('reduce', 2),  # R2: Definiciones ::= ε
    (3, 'Definicion Definiciones'): ('reduce', 3),  # R3: Definiciones ::= Definicion Definiciones
    (2, 'Definiciones'): ('reduce', 1),  # R1: Programa ::= Definiciones
    (1, 'Programa'): ('accept',),
}

# Tabla de transiciones (goto)
goto = {
    (0, 'DefVar'): 4,
    (4, 'Definicion'): 3,
    (3, 'Definiciones'): 2,
    (0, 'Programa'): 1,
}

# Producciones de la gramática
productions = {
    1: ('Programa', 1),
    2: ('Definiciones', 0),
    3: ('Definiciones', 2),
    4: ('Definicion', 1),
    6: ('DefVar', 4),
    7: ('ListaVar', 0),
}

# ======================
# Lexer
# ======================
def lexer(input_string):
    """
    Analizador léxico para dividir la cadena de entrada en tokens reconocibles.
    """
    token_specification = [
        ('Int', r'Int'),          # Tipo de dato Int
        ('ID', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identificadores
        ('SEMICOLON', r';'),      # Punto y coma
        ('SKIP', r'[ \t]+'),      # Espacios en blanco
    ]
    tokens = []
    regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
    for match in re.finditer(regex, input_string):
        kind = match.lastgroup
        value = match.group()
        if kind == 'SKIP':
            continue
        tokens.append((kind, value))
    tokens.append(('$', '$'))  # Fin de la entrada
    return tokens

# ======================
# Parser LR
# ======================
def lr_parser(input_string):
    """
    Analizador LR para procesar cadenas según la gramática y tabla LR definidas.
    """
    tokens = lexer(input_string)
    stack = [0]  # Pila inicial
    index = 0

    print(f"Tokens generados: {tokens}")
    print("\nInicio del análisis...")

    while True:
        state = stack[-1]
        token_type = tokens[index][0]

        print(f"\nPila actual: {stack}")
        print(f"Estado actual: {state}, Token actual: {tokens[index]}")

        if (state, token_type) in action:
            act = action[(state, token_type)]
            if act[0] == 'shift':
                print(f"Shift: desplazando '{tokens[index]}' y moviendo al estado {act[1]}")
                stack.append(tokens[index][0])
                stack.append(act[1])
                index += 1
            elif act[0] == 'reduce':
                prod_num = act[1]
                prod = productions[prod_num]
                print(f"Reduce: aplicando regla {prod_num} -> {prod[0]} ::= {prod[1]}")
                for _ in range(2 * prod[1]):
                    stack.pop()
                state = stack[-1]
                stack.append(prod[0])
                stack.append(goto[(state, prod[0])])
            elif act[0] == 'accept':
                print("Cadena aceptada.")
                return True
        else:
            print(f"Error de sintaxis en el token: {tokens[index]}")
            return False

# ======================
# Pruebas
# ======================
def main():
    """
    Función principal para probar el parser LR.
    """
    print("=== Analizador LR ===\n")
    entrada = input("Ingrese la cadena de entrada: ")
    if lr_parser(entrada):
        print("\nResultado: La cadena es válida según la gramática.")
    else:
        print("\nResultado: La cadena no es válida según la gramática.")

if __name__ == "__main__":
    main()
