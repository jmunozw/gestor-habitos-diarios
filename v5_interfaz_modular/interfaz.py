import tkinter as tk
from gestorHabitos import GestorDeHabitos

class InterfazHabitos:

    def __init__(self, root):
        
        #Nuestra ventana principal
        self.root = root
        self.root.title("Ritual diario")

        #Intanciamos gestor
        self.gestor = GestorDeHabitos()

        #Construimos nuestra interfaz.
        self.construirInterfaz()
    
    def crear_zona_entrada(self):

        #Frame principal
        self.frame_superior = tk.Frame(self.root, bg="lightgray")
        self.frame_superior.pack(pady=10)

        # Creando el campo de entrada de texto
        self.entry = tk.Entry(self.frame_superior)
        self.entry.pack(side=tk.LEFT, padx=15)

        # Creando el botón Añadir habito
        self.btnAñadir = tk.Button(self.frame_superior,text="Añadir hábito", command= self.añadir_habito_gui)
        self.btnAñadir.pack(side=tk.LEFT, padx= 15)

    def crear_zona_lista(self):
        # Creamos un Listbox para visualizar los hábitos
        self.listbox = tk.Listbox(self.root, width=40, height=10)
        self.listbox.pack(pady=10)

        # Vinculando evento listbox y boton
        self.listbox.bind("<<ListboxSelect>>", lambda event: self.habilitar_btnCompletar())


    def crear_zona_botones(self):
        # Creando el botón Completar hábito
        self.btnCompletar = tk.Button(self.root,text="Completar hábito", state = tk.DISABLED, command= self.completar_habito_gui)
        self.btnCompletar.pack(side=tk.TOP,pady=5)

        #Creando label de mensaje
        self.lblMensaje = tk.Label(self.root, text= "", fg="green")
        self.lblMensaje.pack(side=tk.BOTTOM,pady=5)

    def construirInterfaz(self):
    
        self.crear_zona_entrada()
        self.crear_zona_lista()
        self.crear_zona_botones()

        # Insertamos todos los habitos cargados desde el gestorDeHabitos
        self.listar_ListBox()      

        

    def añadir_habito_gui(self):
        nuevoHabito =  self.entry.get()
        mensaje, estado = self.gestor.añadir_habitos(nuevoHabito)

        self.mostrar_mensaje(mensaje,estado)

        if estado == "ok":
            self.entry.delete(0, tk.END)
            self.actualizar_ListBox()
    
    def mostrar_mensaje(self, mensaje, estado):
        color = "green" if estado == "ok" else "red"
        self.lblMensaje.config(text= mensaje, fg= color)
        self.root.after(3000, lambda: self.lblMensaje.config(text=""))

    def actualizar_ListBox(self):
        self.listbox.delete(0, tk.END)
        self.listar_ListBox()

    def listar_ListBox(self):
        for habito in self.gestor.habitos:
            nombre = habito["nombre"]
            completado = "[X]" if habito['completado'] else "[ ]"
            self.listbox.insert(tk.END, f"{nombre}   -   {completado}")

    def completar_habito_gui(self):
        #Obtenemos el indice del habito seleccionado en el listbox
        indice = self.listbox.curselection() # Formato tupla: (indice,)
        mensaje, estado = self.gestor.completar_habito(indice[0])

        self.mostrar_mensaje(mensaje, estado)

        if estado == "ok":
            self.actualizar_ListBox()
    
    def habilitar_btnCompletar(self):
        if self.listbox.curselection():
            self.btnCompletar.config(state= tk.NORMAL)
        else:
            self.btnCompletar.config(state= tk.DISABLED)

