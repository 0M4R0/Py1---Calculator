import tkinter as tk

print("Esto es una calculadora")

class calculator:
    # Constructor de la clase calculator
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root
        self.root.title("Calculadora")  # Título de la ventana
        self.operacion = ""  # Variable para almacenar la operación actual (Como si fuera una array)

        # Esto es para el tamaño de la ventana (width * height)
        # self.root.geometry("400x600") 

        self.resultado_mostrado = False  # Controla si ya se ha mostrado el resultado
        self.texto = tk.StringVar()  # Variable para controlar lo que se muestra en la entrada
        self.crear_widgets()  # Llama a la función para crear los widgets
        # Vincula las teclas del teclado físico con la calculadora
        self.root.bind("<Key>", self.key_event)

    # Crea los widgets de la calculadora (entrada y botones)
    def crear_widgets(self):
        # Entrada donde se muestra la operación y el resultado
        entrada = tk.Entry(self.root, textvariable=self.texto, font=("Arial", 20), bd=10, insertwidth=4, width=15, borderwidth=10, bg="#333", fg="#fff")
        entrada.grid(row=0, column=0, columnspan=4)  # Ubicación de la entrada en la cuadrícula

        # Lista de etiquetas para los botones de la calculadora
        botones = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','.','=','+',
            'C','CE'  # 'C' borra un dígito y 'CE' borra todo
        ]

        fila = 1  # Empieza a partir de la segunda fila (la primera es para la entrada)
        columna = 0  # Primera columna para los botones
        # Crea los botones y los ubica en la cuadrícula
        for boton in botones:
            # Cada botón tiene una acción asociada que llama a la función click_boton
            accion = lambda x=boton: self.click_boton(x)
            btn = tk.Button(self.root, text=boton, padx=15, pady=10, font=("Arial", 18), command=accion)
            btn.grid(row=fila, column=columna)

            # Agregar hover
            btn.bind("<Enter>", lambda event, b=btn: b.config(bg="#a6a6a6")) 
            btn.bind("<Leave>", lambda event, b=btn: b.config(bg="SystemButtonFace"))

            # Mueve el botón a la siguiente columna
            columna += 1
            # Si llega al límite de 4 columnas, salta a la siguiente fila
            if columna > 3:
                columna = 0
                fila += 1

    # Lógica para manejar los clics en los botones
    def click_boton(self, valor):
        # Si se presiona '=', evalúa la operación
        if valor == "=":
            try:
                # Intenta evaluar la operación
                result = str(eval(self.operacion))
                self.texto.set(result)  # Muestra el resultado en la entrada
                self.operacion = result  # El resultado se convierte en la nueva operación
                self.resultado_mostrado = True  # Marca que se mostró un resultado
            except:
                self.texto.set('Error')  # Si hay un error, muestra "Error"
                self.operacion = ""
        # Si se presiona 'C', borra el último carácter o todo si el resultado está mostrado
        elif valor == "C":
            if self.resultado_mostrado:
                self.operacion = ''  # Reinicia la operación
                self.texto.set('')  # Limpia la pantalla
                self.resultado_mostrado = False  # Desactiva el estado de resultado mostrado
            else:
                self.operacion = self.operacion[:-1]  # Elimina el último carácter
                self.texto.set(self.operacion)  # Actualiza la pantalla
        # Si se presiona 'CE', borra todo
        elif valor == "CE":
            self.operacion = ''  # Limpia la operación
            self.texto.set('')  # Limpia la pantalla
            self.resultado_mostrado = False  # Reinicia el estado de resultado mostrado
        # Evita iniciar una operación con un operador matemático
        elif valor in "+*/" and not self.operacion:
            pass
        # Agrega el valor del botón a la operación
        else:
            if self.resultado_mostrado:
                self.operacion = ""  # Si ya se mostró un resultado, inicia una nueva operación
                self.resultado_mostrado = False  # Desactiva el estado de resultado mostrado
            self.operacion += str(valor)  # Agrega el valor presionado
            self.texto.set(self.operacion)  # Muestra la operación en la pantalla

    # Lógica para manejar eventos de teclado
    def key_event(self, event):
        # Define las teclas permitidas para la calculadora
        teclas = "0123456789+-*/.=C"
        # Si la tecla presionada está en la lista, simula un clic en el botón correspondiente
        if event.char in teclas:
            self.click_boton(event.char)
        # Si se presiona "Enter", ejecuta la operación (equivalente a '=')
        elif event.keysym == "Return":
            self.click_boton("=")
        # Si se presiona "Backspace", borra el último carácter (equivalente a 'C')
        elif event.keysym == "BackSpace":
            self.click_boton("C")

# Bloque principal que inicia la calculadora
if __name__ == "__main__":
    root = tk.Tk()  # Crea la ventana principal
    app = calculator(root)  # Instancia la clase calculator
    root.mainloop()  # Inicia el loop principal de la aplicación
