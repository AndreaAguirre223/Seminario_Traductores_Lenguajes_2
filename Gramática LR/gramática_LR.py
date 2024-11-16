import tkinter as tk
from tkinter import scrolledtext
import itertools

class Parser:
    def __init__(self, output_widget=None):
        self.stack = [0]  # Comienza en el estado inicial (0)
        self.table = {
            (0, 'Int'): 'd5',
            (5, 'hola'): 'd8',
            (8, ';'): 'r7',
            (0, ';'): 'd12',  # Estado correcto para manejar el símbolo ';' después de la reducción
            (12, ';'): 'aceptar',  # Estado de aceptación
        }
        self.output_widget = output_widget  # Widget para mostrar los resultados
    
    def log(self, text):
        """ Función para imprimir en la ventana de resultados """
        if self.output_widget:
            self.output_widget.insert(tk.END, text + '\n')
            self.output_widget.yview(tk.END)  # Desplazar al final

    def parse(self, tokens):
        self.log("Cadena de entrada: " + str(tokens))
        
        i = 0  # Índice de los tokens
        while True:
            state = self.stack[-1]  # Último estado en la pila
            symbol = tokens[i] if i < len(tokens) else '$'  # Símbolo actual
            
            self.log(f"Estado actual: {state}, Símbolo actual: {symbol}")
            
            # Verificar si hay una acción definida para el estado actual y el símbolo
            if (state, symbol) in self.table:
                action = self.table[(state, symbol)]
                self.log(f"Acción: {action}")
                
                if action.startswith('d'):  # Desplazamiento
                    next_state = int(action[1:])
                    self.log(f"Desplazando: {symbol}, al estado {next_state}")
                    self.stack.append(next_state)
                    i += 1  # Mover al siguiente token
                elif action.startswith('r'):  # Reducción
                    rule = action
                    self.log(f"Reducción: {rule}")
                    self.reduce(rule)
                elif action == 'aceptar':  # Estado de aceptación
                    self.log("Cadena aceptada")
                    break  # Termina el análisis exitoso
            else:
                self.log(f"Error: No hay acción definida para el estado {state} con el símbolo {symbol}")
                self.log("Cadena no aceptada")
                break
    
    def reduce(self, rule):
        # Reducción para la regla r7: <ListaVar> ::= ε
        if rule == 'r7':  # <ListaVar> ::= ε
            self.stack.pop()  # Eliminamos el símbolo no terminal
            self.stack.pop()  # Eliminamos el símbolo terminal
            state = self.stack[-1]
            self.log(f"Estado después de la reducción r7: {state}")
            
            # Después de la reducción, vamos al estado 0, pero permitimos una transición con ';'
            if (state, ';') in self.table:  # Verifica si el estado permite una transición con ';'
                action = self.table[(state, ';')]
                self.log(f"Transición después de reducción: {action}")
                if action.startswith('d'):
                    next_state = int(action[1:])
                    self.stack.append(next_state)  # Desplazamos al siguiente estado
                elif action == 'aceptar':  # Estado de aceptación
                    self.log("Cadena aceptada")
                    return  # Termina el análisis
            else:
                self.log(f"Error de sintaxis: se esperaba ';' después de la reducción r7")
                return  # Termina el análisis con error


def create_gui():
    # Crear la ventana principal
    window = tk.Tk()
    window.title("Analizador Sintáctico - Resultados")
    window.geometry("850x650")  # Tamaño de la ventana
    window.config(bg="black")  # Fondo base negro para el contraste
    
    # Crear un fondo con degradado de arcoíris
    canvas = tk.Canvas(window, width=850, height=650)
    canvas.place(x=0, y=0)
    
    # Crear un fondo de arcoíris con una transición suave
    rainbow_gradient = itertools.cycle(["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"])
    def animate_background():
        color = next(rainbow_gradient)
        canvas.create_rectangle(0, 0, 850, 650, fill=color, outline="")
        window.after(100, animate_background)
    
    animate_background()  # Iniciar el cambio de color
    
    # Título animado con colores del arco iris
    title_label = tk.Label(window, text="Analizador Sintáctico", font=("Helvetica", 40, "bold"), fg="white", bg="black", relief="flat")
    title_label.pack(pady=20)

    def animate_title():
        rainbow_colors = itertools.cycle(["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"])  # Ciclo de colores del arcoíris
        def change_color():
            color = next(rainbow_colors)
            title_label.config(fg=color)
            window.after(100, change_color)  # Cambiar color cada 100 ms
        
        change_color()  # Iniciar el cambio de color

    animate_title()  # Comenzar la animación
    
    # Área de texto de salida (con bordes redondeados y estilo atractivo)
    output_widget = scrolledtext.ScrolledText(window, width=90, height=20, wrap=tk.WORD, font=("Courier New", 12), bg="black", fg="white", insertbackground="white", relief="flat", bd=5)
    output_widget.pack(padx=30, pady=20)

    # Nuevo diseño de botón 3D con sombra y efectos de presionado
    start_button = tk.Button(window, text="Iniciar Análisis", font=("Arial", 16, "bold"), fg="white", relief="raised", bd=10, width=20, height=2, command=lambda: start_parsing(output_widget))

    # Estilo 3D con sombra y bordes elevados
    start_button.config(
        bg="#FF4500",  # Color de fondo inicial
        activebackground="#FF6347",  # Color al hacer clic
        highlightthickness=0,  # Quitar borde al hacer clic
        relief="raised",  # Efecto de botón elevado
        padx=10, pady=10,
        bd=5,  # Borde grueso
        activeforeground="yellow",
        font=("Arial", 16, "bold")
    )

    # Crear degradado de fondo con bordes redondeados
    start_button.place(x=325, y=500)

    # Efecto de hover para el botón
    def on_enter(event):
        start_button.config(bg="#FF6347", fg="yellow", relief="sunken")  # Cambio de relieve al hacer hover

    def on_leave(event):
        start_button.config(bg="#FF4500", fg="white", relief="raised")  # Volver al relieve normal

    start_button.bind("<Enter>", on_enter)
    start_button.bind("<Leave>", on_leave)

    # Ejecutar la GUI
    window.mainloop()

def start_parsing(output_widget):
    # Crear una instancia del analizador y pasar el widget de salida
    parser = Parser(output_widget)
    
    # Ejemplo de cadena de entrada (tokens)
    tokens = ['Int', 'hola', ';', '$']
    
    # Iniciar el análisis
    parser.parse(tokens)


# Llamar a la función para crear la ventana
create_gui()

