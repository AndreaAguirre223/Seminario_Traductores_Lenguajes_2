from tabulate import tabulate
import tkinter as tk
from tkinter import scrolledtext

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

def imprimir_tabla_en_ventana(datos, titulo):
    ventana = tk.Tk()
    ventana.title(titulo)

    # Cambiar el color de fondo de la ventana
    ventana.configure(bg='#9370DB')  # Morado

    # Crear un marco para el título
    frame_titulo = tk.Frame(ventana, bg='#9370DB')  # Morado
    frame_titulo.pack(pady=10)

    # Título con un estilo atractivo
    label_titulo = tk.Label(frame_titulo, text=titulo, font=("Arial", 18, "bold"), bg='#9370DB', fg='white', padx=10, pady=5, relief=tk.RAISED)
    label_titulo.pack()

    # Efecto de animación
    def fade_out():
        current_color = label_titulo.cget("bg")
        new_color = "#8A2BE2" if current_color == "#9370DB" else "#9370DB"
        label_titulo.config(bg=new_color)
        label_titulo.after(500, fade_out)  # Cambia cada 500 ms

    fade_out()  # Iniciar animación

    # Área de texto desplazable
    text_area = scrolledtext.ScrolledText(ventana, width=100, height=20, bg='#E6E6FA', fg='black')  # Lila
    text_area.pack(padx=10, pady=10)

    tabla = tabulate(datos, headers=["Pila", "Entrada", "Salida"], tablefmt="grid")
    text_area.insert(tk.END, tabla)

    text_area.configure(state='disabled')  # Desactivar edición
    ventana.geometry("1000x400")  # Ajustar el tamaño de la ventana
    ventana.mainloop()

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

        else:
            break
        i += 1
    
    imprimir_tabla_en_ventana(datos, "🔮 Resultados del Primer Ejercicio 🔮")

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

    imprimir_tabla_en_ventana(datos, "✨ Resultados del Segundo Ejercicio ✨")

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

def main():
    print("----------------------------")
    print("Primer Ejercicio: ")
    print("----------------------------")
    primer_ejercicio("hola+mundo$")
    print("----------------------------")
    print("Segundo Ejercicio: ")
    print("----------------------------")
    segundo_ejercicio("a+b+c+d+e+f$")
    print("----------------------------")

if __name__ == "__main__":
    main()
