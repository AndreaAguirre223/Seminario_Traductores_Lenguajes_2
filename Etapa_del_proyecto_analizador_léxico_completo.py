import re
import tkinter as tk
from tkinter import ttk
from tkinter import font

def analizador_lexico(codigo_fuente):
    tokens = []
    estado_actual = 0
    buffer = ""

    tipo = {'int', 'float', 'void'}
    palabras_reservadas = {'if': '19', 'while': '20', 'return': '21', 'else': '22'}

    i = 0

    def agregar_token(simbolo, tipo, valor):
        tokens.append((simbolo, tipo, valor))

    while i < len(codigo_fuente):
        caracter = codigo_fuente[i]

        if estado_actual == 0:
            if caracter.isalpha() or caracter == '_':
                estado_actual = 1
                buffer += caracter
            elif caracter.isdigit():
                estado_actual = 2
                buffer += caracter
            elif caracter == '"':
                estado_actual = 4
                buffer += caracter
            elif caracter in {'+', '-'}:
                agregar_token("Operador de Adición", "5", caracter)
            elif caracter in {'*', '/'}:
                agregar_token("Operador de Multiplicación", "6", caracter)
            elif caracter in {'<', '>'}:
                estado_actual = 7
                buffer += caracter
            elif caracter == '|':
                estado_actual = 8
                buffer += caracter
            elif caracter == '&':
                estado_actual = 9
                buffer += caracter
            elif caracter == '!':
                estado_actual = 10
                buffer += caracter
            elif caracter == '=':
                estado_actual = 11
                buffer += caracter
            elif caracter == ';':
                agregar_token("Punto y coma", "12", caracter)
            elif caracter == ',': 
                agregar_token("Coma", "13", caracter)
            elif caracter == '(':
                agregar_token("Parentesis", '14', caracter)
            elif caracter == ')':
                agregar_token("Parentesis", '15', caracter)
            elif caracter == '{':
                agregar_token("Llave", "16", caracter)
            elif caracter == '}':
                agregar_token("Llave", "17", caracter)
            elif caracter == '$':
                agregar_token("Pesos", "23", caracter)
            elif caracter.isspace():
                i += 1
                continue
            else:
                print(f"Caracter inesperado: {caracter}")
                i += 1
                continue

        elif estado_actual == 1:  # Estado para identificadores
            if caracter.isalnum() or caracter == '_':
                buffer += caracter
            else:
                if buffer in palabras_reservadas:
                    agregar_token("Palabra reservada", palabras_reservadas[buffer], buffer)
                elif buffer in tipo:
                    agregar_token("Tipo", "4", buffer)
                else:
                    agregar_token("Identificador", "0", buffer)
                buffer = ""
                estado_actual = 0
                continue

        elif estado_actual == 2:  # Estado para números
            if caracter.isdigit():
                buffer += caracter
            elif caracter == '.':
                estado_actual = 3
                buffer += caracter
            else:
                agregar_token("Entero", "1", int(buffer))
                buffer = ""
                estado_actual = 0
                continue

        elif estado_actual == 3:  # Estado para números reales
            if caracter.isdigit():
                buffer += caracter
            else:
                agregar_token("Real", "2", float(buffer))
                buffer = ""
                estado_actual = 0
                continue

        elif estado_actual == 4:  # Estado para cadenas
            if caracter == '"':
                buffer += caracter
                agregar_token("Cadena", "3", buffer)
                buffer = ""
                estado_actual = 0
                continue
            else:
                buffer += caracter

        elif estado_actual == 7:  # Estado para operadores relacionales
                if caracter == '=':
                    buffer += caracter
                    agregar_token("Operador relacional", "7", buffer)
                    buffer = ""
                    estado_actual = 0
                else:
                    agregar_token("Operador relacional", "7", buffer)
                    buffer = ""
                    estado_actual = 0
            
        elif estado_actual == 8: # Estado para operador Or
                if caracter == '|':
                    buffer += caracter
                    agregar_token("Operador Or", "8", buffer)
                    buffer = ""
                    estado_actual = 0
                else:
                    print("Caracter Inválido:", buffer)
                    buffer = ""
                    estado_actual = 0

        elif estado_actual == 9: # Estado para operador And
                if caracter == '&':
                    buffer += caracter
                    agregar_token("Operador And", "9", buffer)
                    buffer = ""
                    estado_actual = 0
                else:
                    print("Caracter Inválido:", buffer)
                    buffer = ""
                    estado_actual = 0

        elif estado_actual == 10:  # Estado para operador de igualdad o Not
                if caracter == '=':
                    buffer += caracter
                    agregar_token("Operador de igualdad", "11", buffer)
                    buffer = ""
                    estado_actual = 0
                else:
                    agregar_token("Operador Not", "10", buffer)
                    buffer = ""
                    estado_actual = 0

        elif estado_actual == 11:  # Estado para operador de igualdad o asignación
                if caracter == '=':
                    buffer += caracter
                    agregar_token("Operador de igualdad", "11", buffer)
                    buffer = ""
                    estado_actual = 0
                else:
                    agregar_token("Operador de asignación", "18", buffer)
                    buffer += caracter
                    buffer = ""
                    estado_actual = 0

        if i == len(codigo_fuente) - 1:
            if estado_actual == 1:
                if buffer in palabras_reservadas:
                    agregar_token("Palabra reservada", palabras_reservadas[buffer], buffer)
                elif buffer in tipo:
                    agregar_token("Tipo", "4", buffer)
                else:
                    agregar_token("Identificador", "0", buffer)
            elif estado_actual == 2:
                agregar_token("Entero", "1", int(buffer))
            elif estado_actual == 3:
                agregar_token("Real", "2", float(buffer))
            elif estado_actual == 4:
                agregar_token("Cadena", "3", buffer)
            elif estado_actual == 10:
                agregar_token("Operador Not", "10", buffer)
            elif estado_actual == 11:
                agregar_token("Operador de asignación", "18", buffer)

        i += 1  

    return tokens

def mostrar_tokens_en_tabla(tokens):
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Tabla de Tokens")
    
    # Configurar fondo lila
    ventana.configure(bg='#D8BFD8')  # Lila claro

    # Crear el Treeview para la tabla
    tabla = ttk.Treeview(ventana, columns=("Simbolo", "Código", "Valor"), show="headings")
    
    # Definir las cabeceras de la tabla en negrita
    estilo_negrita = font.Font(weight='bold')
    tabla.heading("Simbolo", text="Simbolo", anchor="center")
    tabla.heading("Código", text="Código", anchor="center")
    tabla.heading("Valor", text="Valor", anchor="center")
    
    # Añadir los datos de los tokens a la tabla
    for token in tokens:
        tabla.insert("", "end", values=token)
    
    # Estilo de la tabla para ocupar todo el espacio
    tabla.column("Simbolo", anchor="center", width=150)
    tabla.column("Código", anchor="center", width=100)
    tabla.column("Valor", anchor="center", width=150)
    
    # Aplicar estilos
    tabla.tag_configure("Simbolo", font=estilo_negrita)
    tabla.tag_configure("Código", font=estilo_negrita)
    tabla.tag_configure("Valor", font=estilo_negrita)

    # Empaquetar la tabla
    tabla.pack(expand=True, fill="both", padx=20, pady=20)
    
    # Mostrar la ventana
    ventana.mainloop()

# Código de prueba
codigo = 'void main() { int num = 42; if (num > 0) return; else return 0; }'
tokens_codigo = analizador_lexico(codigo)
mostrar_tokens_en_tabla(tokens_codigo)
