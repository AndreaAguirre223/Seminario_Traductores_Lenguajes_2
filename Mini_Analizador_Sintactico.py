import tkinter as tk
from tabulate import tabulate

class ElementoPila:
    ERROR = -1
    IDENTIFICADOR = 0
    SIMBOLO = 1
    SIGNOPESO = 2
    E = 3
    INICIAL = 5

    def __init__(self, tipo, simbolo):
        self.tipo = 5
        self.simbolo = simbolo
    
    def __str__(self) -> str:
        return str(self.simbolo)

class Terminal(ElementoPila):
    
    def __init__(self, tipo, simbolo=None):
        self.tipo = tipo
        self.simbolo = simbolo
        if tipo == ElementoPila.SIGNOPESO:
            self.simbolo = '$' 

class NoTerminal(ElementoPila):
    
    def __init__(self, tipo, simbolo):
        super().__init__(tipo, simbolo)

class Estado(ElementoPila):
    
    def __init__(self, tipo, simbolo):
        super().__init__(tipo, simbolo)
    
class Pila:
    items = []

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(len(self.items), item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1] if self.items else None

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def obtener_pila(self):
        return [str(dato) for dato in self.items]

def imprimir_tabla(datos):
    headers = ["Pila", "Entrada", "Salida"]
    return tabulate(datos, headers=headers, tablefmt="grid")

def mostrar_ventana_ejercicio(titulo, texto):
    ventana = tk.Toplevel()
    ventana.title(titulo)
    text_widget = tk.Text(ventana, wrap="word")
    text_widget.insert(tk.END, texto)
    text_widget.pack(expand=True, fill="both")
    ventana.geometry("600x400")

def primer_ejercicio(texto):
    datos = []
    pila = Pila()
    pila.push(NoTerminal(ElementoPila.SIMBOLO, "$0"))
    
    estado = ElementoPila.INICIAL
    d = 2
    lexema = ""

    i = 0
    while i < len(texto):
        c = texto[i]

        if estado == ElementoPila.INICIAL:
            if es_Letra(c) or c == '_':
                estado = ElementoPila.IDENTIFICADOR
                lexema += c
            elif c == '+':
                lexema += c
                pila.push(Terminal(ElementoPila.SIMBOLO, lexema + str(d)))
                d += 1
                estado = ElementoPila.INICIAL
                lexema = ""
                datos.append([pila.obtener_pila(), texto[i:], pila.peek()])
            elif c == '$':
                pila.clear()
                nuevaPila = Pila()
                nuevaPila.push(Estado(ElementoPila.E, "$0E1"))
                datos.append([nuevaPila.obtener_pila(), "$", nuevaPila.peek()])
            else:
                print("ERROR")
                break

        elif estado == ElementoPila.IDENTIFICADOR:
            if es_Letra(c) or isReal(c) or c == '_':
                estado = ElementoPila.IDENTIFICADOR
                lexema += c
            else:
                pila.push(Terminal(ElementoPila.IDENTIFICADOR, lexema + str(d)))
                d += 1
                estado = ElementoPila.INICIAL
                lexema = ""
                i -= 1
                datos.append([pila.obtener_pila(), texto[i:], pila.peek()])
        i += 1
    
    return imprimir_tabla(datos)

def segundo_ejercicio(texto):
    datos = []
    pila = Pila()
    pila.push(NoTerminal(ElementoPila.SIMBOLO, "$0"))

    estado = ElementoPila.INICIAL
    d2 = 2
    d3 = 3
    lexema = ""

    i = 0
    while i < len(texto):
        c = texto[i]

        if estado == ElementoPila.INICIAL:
            if es_Letra(c) or c == '_':
                estado = ElementoPila.IDENTIFICADOR
                lexema += c
            elif c == '+':
                lexema += c
                pila.push(Terminal(ElementoPila.SIMBOLO, lexema + str(d3)))
                estado = ElementoPila.INICIAL
                lexema = ""
                datos.append([pila.obtener_pila(), texto[i:], pila.peek()])
            elif c == '$':
                pila.clear()
                nuevaPila = Pila()
                nuevaPila.push(Estado(ElementoPila.E, "$0E1"))
                datos.append([nuevaPila.obtener_pila(), "$", nuevaPila.peek()])
            else:
                print("ERROR")
                break

        elif estado == ElementoPila.IDENTIFICADOR:
            if es_Letra(c) or isReal(c) or c == '_':
                estado = ElementoPila.IDENTIFICADOR
                lexema += c
            else:
                pila.push(Terminal(ElementoPila.IDENTIFICADOR, lexema + str(d2)))
                estado = ElementoPila.INICIAL
                lexema = ""
                i -= 1
                datos.append([pila.obtener_pila(), texto[i:], pila.peek()])
        i += 1

    return imprimir_tabla(datos)

def isReal(c):
    if 48 <= ord(c) <= 57:
        return True
    else:
        return False

def es_Letra(c):
    if (65 <= ord(c) <= 90 or ord(c) == 95) or (97 <= ord(c) <= 122 or ord(c) == 95):
        return True
    else:
        return False

def aplicar_degradado(event, boton, colores):
    for i, color in enumerate(colores):
        boton.after(50 * i, lambda col=color: boton.config(bg=col))

def revertir_color(event, boton, color_normal):
    boton.config(bg=color_normal)

def main():
    root = tk.Tk()
    root.title("Ejercicios")

    # Definir colores para el degradado
    color_morado1 = "#6A0DAD"
    color_morado2 = "#7D26CD"
    color_morado3 = "#8A2BE2"
    color_morado4 = "#9A4DFF"
    colores_degradado = [color_morado1, color_morado2, color_morado3, color_morado4]
    
    # Cambiar tamaño y estilo de letra
    btn_font = ("Helvetica", 14, "bold")
    btn_width = 30  # Aumentar el ancho del botón

    # Botón para el primer ejercicio
    btn1 = tk.Button(root, text="MOSTRAR PRIMER EJERCICIO", 
                     command=lambda: mostrar_ventana_ejercicio("Primer Ejercicio", primer_ejercicio("hola+mundo$")),
                     bg=color_morado1, fg="white", font=btn_font, width=btn_width, bd=5, relief="raised")
    btn1.pack(pady=10)
    btn1.bind("<Enter>", lambda e: aplicar_degradado(e, btn1, colores_degradado))
    btn1.bind("<Leave>", lambda e: revertir_color(e, btn1, color_morado1))

    # Botón para el segundo ejercicio
    btn2 = tk.Button(root, text="MOSTRAR SEGUNDO EJERCICIO", 
                     command=lambda: mostrar_ventana_ejercicio("Segundo Ejercicio", segundo_ejercicio("a+b+c+d+e+f$")),
                     bg=color_morado1, fg="white", font=btn_font, width=btn_width, bd=5, relief="raised")
    btn2.pack(pady=10)
    btn2.bind("<Enter>", lambda e: aplicar_degradado(e, btn2, colores_degradado))
    btn2.bind("<Leave>", lambda e: revertir_color(e, btn2, color_morado1))

    # Configuración de la ventana principal (más grande para ver los botones completos)
    root.geometry("400x300")
    root.mainloop()

if __name__ == "__main__":
    main()




