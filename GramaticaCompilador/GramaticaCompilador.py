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
archivo = open('C:\\Users\\andre\\OneDrive\\Escritorio\\Seminario de Traductores de Lenguaje 2\\GramaticaCompilador\\compilador.lr', 'r')
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
        listaEstados = []

        for char in self.string:
            ascii = ord(char)
            if (estado == 0):
                if(ascii > 47 and ascii < 58):
                    estado = 1
                    aux+=char
                elif (ascii> 64 and ascii < 91) or (ascii>96 and ascii<123):
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
                    aux+=char
                    break
            elif (estado==1):
                if(ascii > 47 and ascii < 58):
                    estado = 1
                    aux+=char
                elif(ascii == 46):
                    estado = 2
                    aux+=char
                elif (ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break
            elif (estado==2):
                if(ascii > 47 and ascii < 58):
                    estado = 3
                    aux+=char
                else:
                    aux+=char
                    break
            elif (estado==3):
                if(ascii > 47 and ascii < 58):
                    estado = 3
                    aux+=char
                elif (ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break
            elif(estado==4):
                if(ascii > 47 and ascii < 58):
                    aux+=char
                    estado = 4
                    aux+=char
                elif (ascii> 64 and ascii < 91) or (ascii>96 and ascii<123):
                    estado = 4
                    aux+=char
                elif(aux == 'int'):
                    state = Estado(aux, 25)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif(aux == "float"):
                    state = Estado(aux, 26)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif (aux == "void"):
                    state = Estado(aux, 27)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif(aux == "if"):
                    state = Estado(aux, 28)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif(aux == "while"):
                    state = Estado(aux, 29)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif (aux == "return"):
                    state = Estado(aux, 30)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif(aux == "else"):
                    state = Estado(aux, 31)
                    listaEstados.append(state)
                    estado = 0
                    aux = ""
                elif (ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break
            elif(estado==5):
                if(ascii > 47 and ascii < 58):
                    estado = 5
                    aux+=char
                elif (ascii> 64 and ascii < 91) or (ascii>96 and ascii<123):
                    estado = 5
                    aux+=char
                elif(ascii == 32):
                    estado = 5
                    aux+=char
                elif(ascii == 39):
                    estado = 6
                    aux+=char
                else:
                    aux+=char
                    break
            elif(estado == 6):
                if (ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break
            elif(estado == 7):
                if (ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break
            elif(estado == 8):
                if (ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break
            elif(estado == 9):                
                if (ascii==61):
                    estado = 10
                    aux+=char
                elif(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break
            elif(estado == 10):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break    
            elif(estado == 11):                
                if(ascii==124):
                    estado = 12
                    aux+=char
                else:
                    aux+=char
                    break  
            elif(estado == 12):                
                if(ascii==32):
                    aux+=char
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break 
            elif(estado == 13):                
                if(ascii==38):
                    estado = 14
                    aux+=char
                else:
                    aux+=char
                    break  
            elif(estado == 14):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break      
            elif(estado == 15):                
                if(ascii == 61):
                    estado = 16
                    aux+=char
                elif(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break       
            elif(estado == 16):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break     
            elif(estado == 17):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                elif(ascii == 61):
                    estado = 16
                    aux+=char
                else:
                    aux+=char
                    break      
            elif(estado == 18):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break 
            elif(estado == 19):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break  
            elif(estado == 20):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break  
            elif(estado == 21):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break    
            elif(estado == 22):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break  
            elif(estado == 23):                
                if(ascii==32):
                    aux+=char
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    aux+=char
                    break     
            elif(estado == 24):                
                if(ascii==32):
                    state = Estado(aux, estado)
                    listaEstados.append(state)
                    aux = ""
                    estado = 0
                else:
                    break
        print("Aux:", aux)
        state = Estado(aux, estado)
        listaEstados.append(state)
        return listaEstados
             
cadena = "float calculateAverage ( int a , int b ) { return ( a + b ) / 2.0 ; } $"
estados = []
tokens = []
lexicos = []
listaDeEstados = Lexico(cadena).léxico()
i = 0
valoresTokens = []
print("Tamaño de lista de estados: ", len(listaDeEstados))
while i < len(listaDeEstados):
    tipo = listaDeEstados[i].tipo
    fuente = listaDeEstados[i].fuente
    if(listaDeEstados[i].tipo==0):
        mensaje = listaDeEstados[i].fuente, "no es válido"
        terminal = Terminal(listaDeEstados[i].fuente, listaDeEstados[i].tipo)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==1):
        mensaje = listaDeEstados[i].fuente, "es un: entero"
        terminal = Terminal(listaDeEstados[i].fuente, 1)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==3):
        mensaje = listaDeEstados[i].fuente, "es un: real"
        terminal = Terminal(listaDeEstados[i].fuente, 2)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==4):
        mensaje = listaDeEstados[i].fuente, "es un: identificador"
        terminal = Terminal(listaDeEstados[i].fuente, 0)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==6):
        mensaje = listaDeEstados[i].fuente, "es un: string"
        terminal = Terminal(listaDeEstados[i].fuente, 3)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==7):
        mensaje = listaDeEstados[i].fuente, "es un: operador Suma"
        terminal = Terminal(listaDeEstados[i].fuente, 5)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==8):
        mensaje = listaDeEstados[i].fuente, "es un: operador Multiplicación"
        terminal = Terminal(listaDeEstados[i].fuente, 6)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==9 or listaDeEstados[i].tipo==10):
        mensaje = listaDeEstados[i].fuente, "es un: operador Relacional"
        terminal = Terminal(listaDeEstados[i].fuente, 7)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==12):
        mensaje = listaDeEstados[i].fuente, "es un: operador OR"
        terminal = Terminal(listaDeEstados[i].fuente, 8)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==14):
        mensaje = listaDeEstados[i].fuente, "es un: operador AND"
        terminal = Terminal(listaDeEstados[i].fuente, 9)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==15):
        mensaje = listaDeEstados[i].fuente, "es un: operador NOT"
        terminal = Terminal(listaDeEstados[i].fuente, 10)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==16):
        mensaje = listaDeEstados[i].fuente, "es un: operador IGUALDAD"
        terminal = Terminal(listaDeEstados[i].fuente, 11)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==17):
        mensaje = listaDeEstados[i].fuente, "es un: símbolo igualdad"
        terminal = Terminal(listaDeEstados[i].fuente, 18)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==18):
        mensaje = listaDeEstados[i].fuente, "es un: punto y coma"
        terminal = Terminal(listaDeEstados[i].fuente, 12)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==19):
        mensaje = listaDeEstados[i].fuente, "es una: coma"
        terminal = Terminal(listaDeEstados[i].fuente, 13)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==20):
        mensaje = listaDeEstados[i].fuente, "es un: paréntesis de apertura"
        terminal = Terminal(listaDeEstados[i].fuente, 14)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==21):
        mensaje = listaDeEstados[i].fuente, "es un: paréntesis de cierre"
        terminal = Terminal(listaDeEstados[i].fuente, 15)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==22):
        mensaje = listaDeEstados[i].fuente, "es una: llave de apertura"
        terminal = Terminal(listaDeEstados[i].fuente, 16)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==23):
        mensaje = listaDeEstados[i].fuente, "es una: llave de clausura"
        terminal = Terminal(listaDeEstados[i].fuente, 17)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==24):
        mensaje = listaDeEstados[i].fuente, "es un: EOF"
        terminal = Terminal(listaDeEstados[i].fuente, 23)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==25):
        mensaje = listaDeEstados[i].fuente, "es palabra reservada: int"
        terminal = Terminal(listaDeEstados[i].fuente, 4)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==26):
        mensaje = listaDeEstados[i].fuente, "es palabra reservada: float"
        terminal = Terminal(listaDeEstados[i].fuente, 4)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==27):
        mensaje = listaDeEstados[i].fuente, "es palabra reservada: void"
        terminal = Terminal(listaDeEstados[i].fuente, 4)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==28):
        mensaje = listaDeEstados[i].fuente, "es palabra reservada: if"
        terminal = Terminal(listaDeEstados[i].fuente, 19)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==29):
        mensaje = listaDeEstados[i].fuente, "es palabra reservada: while"
        terminal = Terminal(listaDeEstados[i].fuente, 20)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==30):
        mensaje = listaDeEstados[i].fuente, "es palabra reservada: return"
        terminal = Terminal(listaDeEstados[i].fuente, 21)
        listaTerminales.append(terminal)
    elif(listaDeEstados[i].tipo==31):
        mensaje = listaDeEstados[i].fuente, "es palabra reservada: else"
        terminal = Terminal(listaDeEstados[i].fuente, 22)
        listaTerminales.append(terminal) 
    lexicos.append([tipo, fuente, mensaje])
    i+=1

print(tabulate(lexicos, headers=["Tipo", "Fuente", "Mensaje"], tablefmt="grid"))

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
acciones = []
data = []
pila.append(Terminal("$", 100))
pila.append(Estado("", 0))


while True:
    obj = listaTerminales[i]
    fila = pila[-1]
    print("\n")
    columna = obj.tipo
    accion = tlr1[fila.tipo][columna]
    acciones.append([obj.fuente, accion])
    print(tabulate(acciones, headers=["Objeto", "Accion"], tablefmt="grid"))

    if (accion == 0):
        acc = "NADA"
        print("NADA")
        break
    elif (accion > 0):
        i+=1
        acc = "d"+str(accion)
        pila.append(Terminal(obj.fuente, obj.tipo))
        print("ACC", accion)
        pila.append(Estado("", accion))
    elif (accion == -1):
        acc = "r0(acept)"
        print("R0")
        break
    else:
        acc = "r"+str(abs(accion+1))
        for obj2 in reglas:
            if (accion == (obj2.num + 1)*-1):
                acc = "r"+str(obj2.num)
                accion = tlr1[fila.tipo][obj2.num2]
                if obj2.elem !=0:
                    elim = obj2.elem*2
                    while elim !=0:
                        pila.pop()
                        elim -=1
                    fila = pila[-1]
                    accion = tlr1[fila.tipo][obj2.num2]
                    pila.append(obj2)
                    pila.append(Estado("", accion))
                else:
                    print("obb", obj.fuente)
                    pila.append(obj2)
                    pila.append(Estado("", accion))
                break
    if(i == len(listaTerminales)):
        print("FIN")    

    for p in pila:
        pilaS += str(p.fuente)
    data.append([pilaS, obj.fuente, acc])
    pilaS = ""

print("\n")
print(tabulate(data, headers=["Pila", "Entrada", "Salida"], tablefmt="grid"))