
import tkinter as tk
from tkinter import ttk

# Definición de clases de ejemplo
class Terminal:
    def __init__(self, fuente, tipo):
        self.fuente = fuente
        self.tipo = tipo

class Estado:
    def __init__(self, fuente, tipo):
        self.fuente = fuente
        self.tipo = tipo

class Regla:
    def __init__(self, num, num2, elem):
        self.num = num
        self.num2 = num2
        self.elem = elem

# Datos de ejemplo (reemplaza con tus datos reales)
tlr1 = [
    [2, 0, 0, 1],
    [0, 0, -1, 0],
    [0, 3, -3, 0],
    [2, 0, 0, 4],
    [0, 0, -2, 0]
]

listaTerminales = [
    Terminal("void", 27),
    Terminal("menu", 4),
    Terminal("(", 20),
    Terminal(")", 21),
    Terminal("{", 22),
    Terminal("hola", 4),
    Terminal("=", 17),
    Terminal("5", 1),
    Terminal(";", 18),
    Terminal("}", 23),
    Terminal("$", 24),
]

reglas = [
    Regla(0, 1, 2),  # Reemplaza con tus reglas reales
    # Agrega más reglas según sea necesario
]

# Función para mostrar los resultados
def mostrar_resultados():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Resultados del Análisis Sintáctico")

    # Establecer el tamaño de la ventana
    ventana.geometry("800x600")

    # Personalización del fondo de la ventana
    ventana.configure(bg='#7f4b8d')  # Morado oscuro

    # Crear un encabezado con estilo
    encabezado = tk.Label(ventana, text="Análisis Sintáctico LR(1)", font=("Helvetica", 16, "bold"), fg="white", bg='#7f4b8d')
    encabezado.pack(pady=10)

    # Crear un frame para los resultados y la tabla
    frame_resultados = tk.Frame(ventana, bg='#7f4b8d')
    frame_resultados.pack(fill="both", expand=True)

    # Crear un widget Text para mostrar los mensajes (lo que normalmente saldría en la terminal)
    texto = tk.Text(frame_resultados, height=10, width=80, wrap=tk.WORD, bg="#f0f0f0", font=("Courier", 10))
    texto.pack(pady=10)

    # Insertar algunos ejemplos de mensajes que normalmente imprimirías en la terminal
    texto.insert(tk.END, "Algo salió mal\n")
    texto.insert(tk.END, "Aux: $\n")
    texto.insert(tk.END, "Len lista de estados:  11\n")
    texto.insert(tk.END, "Tipo:  27\n")
    texto.insert(tk.END, "Fuente: void\n")
    texto.insert(tk.END, "void es palabra reservada: void\n")
    texto.insert(tk.END, "Tipo:  4\n")
    texto.insert(tk.END, "Fuente: menu\n")
    texto.insert(tk.END, "menu es un: identificador\n")
    texto.insert(tk.END, "Tipo:  20\n")
    texto.insert(tk.END, "Fuente: (\n")
    texto.insert(tk.END, "( es un: paréntesis de apertura\n")
    texto.insert(tk.END, "Tipo:  21\n")
    texto.insert(tk.END, "Fuente: )\n")
    texto.insert(tk.END, ") es un: paréntesis de cierre\n")
    texto.insert(tk.END, "Tipo:  22\n")
    texto.insert(tk.END, "Fuente: {\n")
    texto.insert(tk.END, "{ es una: llave de apertura\n")
    texto.insert(tk.END, "Tipo:  4\n")
    texto.insert(tk.END, "Fuente: hola\n")
    texto.insert(tk.END, "hola es un: identificador\n")
    texto.insert(tk.END, "Tipo:  17\n")
    texto.insert(tk.END, "Fuente: =\n")
    texto.insert(tk.END, "= es un: símbolo igualdad\n")
    texto.insert(tk.END, "Tipo:  1\n")
    texto.insert(tk.END, "Fuente: 5\n")
    texto.insert(tk.END, "5 es un: entero\n")
    texto.insert(tk.END, "Tipo:  18\n")
    texto.insert(tk.END, "Fuente: ;\n")
    texto.insert(tk.END, "; es un: punto y coma\n")
    texto.insert(tk.END, "Tipo:  23\n")
    texto.insert(tk.END, "Fuente: }\n")
    texto.insert(tk.END, "} es una: llave de clausura\n")
    texto.insert(tk.END, "Tipo:  24\n")
    texto.insert(tk.END, "Fuente: $\n")
    texto.insert(tk.END, "$ es un: EOF\n")

    # Crear la tabla de resultados
    frame_tabla = tk.Frame(ventana, bg='#7f4b8d')
    frame_tabla.pack(fill="both", expand=True)

    tree = ttk.Treeview(frame_tabla, columns=("Pila", "Entrada", "Salida"), show="headings", height=10)

    tree.heading("Pila", text="Pila", anchor="w")
    tree.heading("Entrada", text="Entrada", anchor="w")
    tree.heading("Salida", text="Salida", anchor="w")

    tree.column("Pila", width=150, anchor="w")
    tree.column("Entrada", width=150, anchor="w")
    tree.column("Salida", width=200, anchor="w")

    # Insertar los datos de ejemplo en la tabla
    for fila in listaTerminales:
        tree.insert("", "end", values=(fila.fuente, fila.tipo, "Acción"))

    # Barra de desplazamiento para la tabla
    scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    tree.pack(fill="both", expand=True)

    # Botón para cerrar la ventana
    cerrar_btn = tk.Button(ventana, text="Cerrar", command=ventana.quit, font=("Helvetica", 12), fg="white", bg="#6a3d92")
    cerrar_btn.pack(pady=20)

    ventana.mainloop()

# Llamar a la función para mostrar la ventana
mostrar_resultados()







from tabulate import tabulate 

class ElementoPila:
    def __init__(self, fuente, tipo):
        self.fuente = fuente
        self.tipo = tipo

class Terminal(ElementoPila):
    def __init__(self, fuente, tipo):
        super().__init__(fuente, tipo)

class NoTerminal(ElementoPila):
    def __init__(self, fuente, tipo):
        super().__init__(fuente, tipo)

class Estado(ElementoPila):
    def __init__(self, fuente, tipo):
        super().__init__(fuente, tipo)

listaEstados = []
listaTerminales = []
archivo = open('C:\\Users\\andre\\OneDrive\\Escritorio\\Seminario de Traductores de Lenguaje 2\\Etapa_Arbol_Sintactico\\compilador.lr', 'r')
lines = archivo.readlines()
pila = list()
pilaS = ""
tlr1 = list()
num = 0
reglas  = list()
reg = 0

class Regla:
    def __init__(self, num, num2, elem, fuente):
        self.num = num
        self.num2 = num2
        self.elem = elem
        self.fuente = fuente

for line in lines:
    line = line.rstrip()
    line = line.split("\t")
    if (reg == 1):
        tlr1.append(line)
        for i in range(len(tlr1)):
            for j in range(len(tlr1[i])):
                tlr1[i][j] = int(tlr1[i][j])
    if (line[0]=='52'):
        continue
    if (line[0]=='95'):
        reg = 1
    if (reg == 0):
        num += 1
        obj = Regla(num, int(line[0]), int(line[1]), line[2])
        reglas.append(obj)


class Lexico:
    def __init__(self, string):
        self.string = string + '$'

    def léxico(self):
        estado = 0
        aux = ""
        i = 0
        listaTokens = []
        listaEstados = []

        #print("String a analizar", cadena)
        #print("Tamaño de cadena", len(cadena))
        for char in self.string:
            ascii = ord(char)
            if (estado == 0):
                if(ascii > 47 and ascii < 58):
                    #print("Es número")
                    estado = 1
                    aux+=char
                elif (ascii> 64 and ascii < 91) or (ascii>96 and ascii<123):
                    #print("Es letra")
                    estado = 4
                    aux+=char
                elif(ascii == 39):
                    estado = 5
                    aux+=char
                elif(ascii == 43 or ascii == 45):
                    estado = 7
                    aux+=char
                elif(ascii == 42 or ascii == 47):
                    estado = 8
                    aux+=char
                elif(ascii == 60 or ascii == 62):
                    estado = 9
                    aux+=char
                elif(ascii == 124):
                    estado = 11
                    aux+=char
                elif(ascii == 38):
                    estado = 13
                    aux+=char
                elif(ascii == 33):
                    estado = 15
                    aux+=char
                elif(ascii == 61):
                    estado = 17
                    aux+=char
                elif(ascii == 59):
                    estado = 18
                    aux+=char
                elif(ascii == 44):
                    estado = 19
                    aux+=char
                elif(ascii == 40):
                    estado = 20
                    aux+=char
                elif(ascii == 41):
                    estado = 21
                    aux+=char
                elif(ascii == 123):
                    estado = 22
                    aux+=char
                elif(ascii == 125):
                    estado = 23
                    aux+=char
                elif(ascii == 36):
                    estado = 24
                    aux+=char
                else:
                    print("Algo salió mal")
                    break
            elif (estado==1):
                if(ascii > 47 and ascii < 58):
                    #print("Es número")
                    estado = 1
                    aux+=char
                elif(ascii == 46):
                    #print("Es punto")
                    estado = 2
                    aux+=char
                elif (ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break
            elif (estado==2):
                if(ascii > 47 and ascii < 58):
                    #print("Es número")
                    estado = 3
                    aux+=char
                else:
                    print("Algo salió mal")
                    break
            elif (estado==3):
                if(ascii > 47 and ascii < 58):
                    #print("Es número")
                    estado = 3
                    aux+=char
                elif (ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break
            elif(estado==4):
                if(ascii > 47 and ascii < 58):
                    #print("Es número")
                    estado = 4
                    aux+=char
                elif (ascii> 64 and ascii < 91) or (ascii>96 and ascii<123):
                    #print("Es letra")
                    estado = 4
                    aux+=char
                elif(aux == 'int'):
                    # listaEstados.append(25)
                    # listaTokens.append(aux)
                    state = Estado(aux, 25)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif(aux == "float"):
                    # listaEstados.append(26)
                    # listaTokens.append(aux)
                    state = Estado(aux, 26)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif (aux == "void"):
                    # listaEstados.append(27)
                    # listaTokens.append(aux)
                    state = Estado(aux, 27)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif(aux == "if"):
                    # listaEstados.append(28)
                    # listaTokens.append(aux)
                    state = Estado(aux, 28)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif(aux == "while"):
                    # listaEstados.append(29)
                    # listaTokens.append(aux)
                    state = Estado(aux, 29)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif (aux == "return"):
                    # listaEstados.append(30)
                    # listaTokens.append(aux)
                    state = Estado(aux, 30)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif(aux == "else"):
                    # listaEstados.append(31)
                    # listaTokens.append(aux)
                    state = Estado(aux, 31)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif (ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break
            elif(estado==5):
                if(ascii > 47 and ascii < 58):
                    #print("Es número")
                    estado = 5
                    aux+=char
                elif (ascii> 64 and ascii < 91) or (ascii>96 and ascii<123):
                    #print("Es letra")
                    estado = 5
                    aux+=char
                elif(ascii == 32):
                    estado = 5
                    aux+=char
                elif(ascii == 39):
                    estado = 6
                    aux+=char
                else:
                    print("Algo salió mal")
                    break
            elif(estado == 6):
                if (ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break
            elif(estado == 7):
                if (ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break
            elif(estado == 8):
                if (ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break
            elif(estado == 9):                
                if (ascii==61):
                    estado = 10
                    aux+=char
                elif(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break
            elif(estado == 10):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break    
            elif(estado == 11):                
                if(ascii==124):
                    estado = 12
                    aux+=char
                else:
                    print("Algo salió mal")
                    break  
            elif(estado == 12):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break 
            elif(estado == 13):                
                if(ascii==38):
                    estado = 14
                    aux+=char
                else:
                    print("Algo salió mal")
                    break  
            elif(estado == 14):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break      
            elif(estado == 15):                
                if(ascii == 61):
                    estado = 16
                    aux+=char
                elif(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break       
            elif(estado == 16):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break     
            elif(estado == 17):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                elif(ascii == 61):
                    estado = 16
                    aux+=char
                else:
                    print("Algo salió mal")
                    break      
            elif(estado == 18):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break 
            elif(estado == 19):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break  
            elif(estado == 20):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break  
            elif(estado == 21):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break    
            elif(estado == 22):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break  
            elif(estado == 23):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break     
            elif(estado == 24):                
                if(ascii==32):
                    # listaEstados.append(estado)
                    # listaTokens.append(aux)
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    print("Algo salió mal")
                    break
        # listaEstados.append(estado)
        # listaTokens.append(aux)
        print("Aux:", aux)
        state = Estado(aux, estado)
        listaEstados.append(state)
        #print("Caracter", aux)
        # print("Lista de tokens: ", listaTokens)
        # print("Lista de estados: ", listaEstados)
        return listaEstados

                
cadena = "void menu ( ) { hola = 5 ; } $"
estados = []
tokens = []
# listaDeEstados = []
listaDeEstados = Lexico(cadena).léxico()
#print("Estado", estado, "Cadena", stringFinal)
i = 0
valoresTokens = []
print("Len lista de estados: ", len(listaDeEstados))
while i < len(listaDeEstados):
    print("Tipo: ", listaDeEstados[i].tipo)
    print("Fuente: ", listaDeEstados[i].fuente)
    if(listaDeEstados[i].tipo==0):
        print(listaDeEstados[i].fuente, "no es válido")
        terminal = Terminal(listaDeEstados[i].fuente, listaDeEstados[i].tipo)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==1):
        print(listaDeEstados[i].fuente, "es un: entero")
        terminal = Terminal(listaDeEstados[i].fuente, 1)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==3):
        print(listaDeEstados[i].fuente, "es un: real")
        terminal = Terminal(listaDeEstados[i].fuente, 2)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==4):
        print(listaDeEstados[i].fuente, "es un: identificador")
        terminal = Terminal(listaDeEstados[i].fuente, 0)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==6):
        print(listaDeEstados[i].fuente, "es un: string")
        terminal = Terminal(listaDeEstados[i].fuente, 3)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==7):
        print(listaDeEstados[i].fuente, "es un: operador Suma")
        terminal = Terminal(listaDeEstados[i].fuente, 5)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==8):
        print(listaDeEstados[i].fuente, "es un: operador Multiplicación")
        terminal = Terminal(listaDeEstados[i].fuente, 6)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==9 or listaDeEstados[i].tipo==10):
        print(listaDeEstados[i].fuente, "es un: operador Relacional")
        terminal = Terminal(listaDeEstados[i].fuente, 7)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==12):
        print(listaDeEstados[i].fuente, "es un: operador OR")
        terminal = Terminal(listaDeEstados[i].fuente, 8)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==14):
        print(listaDeEstados[i].fuente, "es un: operador AND")
        terminal = Terminal(listaDeEstados[i].fuente, 9)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==15):
        print(listaDeEstados[i].fuente, "es un: operador NOT")
        terminal = Terminal(listaDeEstados[i].fuente, 10)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==16):
        print(listaDeEstados[i].fuente, "es un: operador IGUALDAD")
        terminal = Terminal(listaDeEstados[i].fuente, 11)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==17):
        print(listaDeEstados[i].fuente, "es un: símbolo igualdad")
        terminal = Terminal(listaDeEstados[i].fuente, 18)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==18):
        print(listaDeEstados[i].fuente, "es un: punto y coma")
        terminal = Terminal(listaDeEstados[i].fuente, 12)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==19):
        print(listaDeEstados[i].fuente, "es una: coma")
        terminal = Terminal(listaDeEstados[i].fuente, 13)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==20):
        print(listaDeEstados[i].fuente, "es un: paréntesis de apertura")
        terminal = Terminal(listaDeEstados[i].fuente, 14)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==21):
        print(listaDeEstados[i].fuente, "es un: paréntesis de cierre")
        terminal = Terminal(listaDeEstados[i].fuente, 15)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==22):
        print(listaDeEstados[i].fuente, "es una: llave de apertura")
        terminal = Terminal(listaDeEstados[i].fuente, 16)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==23):
        print(listaDeEstados[i].fuente, "es una: llave de clausura")
        terminal = Terminal(listaDeEstados[i].fuente, 17)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==24):
        print(listaDeEstados[i].fuente, "es un: EOF")
        terminal = Terminal(listaDeEstados[i].fuente, 23)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==25):
        print(listaDeEstados[i].fuente, "es palabra reservada: int")
        terminal = Terminal(listaDeEstados[i].fuente, 4)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==26):
        print(listaDeEstados[i].fuente, "es palabra reservada: float")
        terminal = Terminal(listaDeEstados[i].fuente, 4)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==27):
        print(listaDeEstados[i].fuente, "es palabra reservada: void")
        terminal = Terminal(listaDeEstados[i].fuente, 4)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==28):
        print(listaDeEstados[i].fuente, "es palabra reservada: if")
        terminal = Terminal(listaDeEstados[i].fuente, 19)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==29):
        print(listaDeEstados[i].fuente, "es palabra reservada: while")
        terminal = Terminal(listaDeEstados[i].fuente, 20)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==30):
        print(listaDeEstados[i].fuente, "es palabra reservada: return")
        terminal = Terminal(listaDeEstados[i].fuente, 21)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==31):
        print(listaDeEstados[i].fuente, "es palabra reservada: else")
        terminal = Terminal(listaDeEstados[i].fuente, 22)
        listaTerminales.append(terminal) 
    i+=1

LR1 = [[2,0,0,1],
        [0,0,-1,0],
        [0,3,0,0],
        [4,0,0,0],
        [0,0,-2,0]]

LR2 = [[2,0,0,1],
        [0,0,-1,0],
        [0,3,-3,0],
        [2,0,0,4],
        [0,0,-2,0]]



fila = 0
columna = 0
datosFin = []
i = 0
data = []
pila.append(Terminal("$", 100))
pila.append(Estado("", 0))


# Verifica que 'tlr1' esté correctamente inicializado
print(f"Longitud de tlr1: {len(tlr1)}")  # Verifica cuántas filas tiene la matriz

# Recorre la lista de terminales
while True:
    obj = listaTerminales[i]
    fila = pila[-1]

    print("OBJETO", obj.fuente)
    columna = obj.tipo

    # Verificación de índices antes de acceder a la matriz
    if fila.tipo < 0 or fila.tipo >= len(tlr1):
        print(f"Índice fila.tipo fuera de rango: {fila.tipo}")
        break

    if columna < 0 or columna >= len(tlr1[fila.tipo]):
        print(f"Índice columna fuera de rango: {columna}")
        break

    # Ahora accedes con seguridad a la matriz
    accion = tlr1[fila.tipo][columna]
    print(f"Acción tomada: {accion}")

    # Procesa las acciones según el valor de `accion`
    if accion == 0:
        acc = "NADA"
        print("NADA")
        break
    elif accion > 0:
        i += 1
        acc = f"d{accion}"
        pila.append(Terminal(obj.fuente, obj.tipo))
        print(f"Desplazar: {accion}")
        pila.append(Estado("", accion))
    elif accion == -1:
        acc = "r0(acept)"
        print("R0")
        break
    else:
        acc = f"r{abs(accion + 1)}"
        for obj2 in reglas:
            if accion == (obj2.num + 1) * -1:
                acc = f"r{obj2.num}"
                accion = tlr1[fila.tipo][obj2.num2]
                
                # Verificación y ajuste según las reglas
                if obj2.elem != 0:
                    elim = obj2.elem * 2
                    while elim != 0:
                        pila.pop()
                        elim -= 1
                    fila = pila[-1]
                    accion = tlr1[fila.tipo][obj2.num2]
                    pila.append(obj2)
                    pila.append(Estado("", accion))
                else:
                    print("Objeto:", obj.fuente)
                    pila.append(obj2)
                    pila.append(Estado("", accion))
                break

    # Verificación de fin
    if i == len(listaTerminales):
        print("FIN")

    pilaS = ""
    for p in pila:
        pilaS += str(p.fuente)
    
    data.append([pilaS, obj.fuente, acc])

# Mostrar los resultados de la tabla
from tabulate import tabulate
print(tabulate(data, headers=["Pila", "Entrada", "Salida"]))
