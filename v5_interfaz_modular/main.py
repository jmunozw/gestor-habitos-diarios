import tkinter as tk
from interfaz import InterfazHabitos



if __name__ == "__main__":
    root = tk.Tk() #Creamos la ventana raiz
    app = InterfazHabitos(root) #Enviamos la ventana a la clase InterfazHabitos
    root.mainloop() #Lanzamos la ventana creada.
