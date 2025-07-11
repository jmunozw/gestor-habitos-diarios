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

        # Vinculando evento listbox y los botones completar y eliminar
        self.listbox.bind("<<ListboxSelect>>", lambda event: self.habilitar_botones())


    def crear_zona_botones(self):
        # Creando el botón Completar hábito
        self.btnCompletar = tk.Button(self.root,text="Completar hábito", state = tk.DISABLED, command= self.completar_habito_gui)
        self.btnCompletar.pack(side=tk.TOP,pady=5)

        #Creando el botón Eliminar hábito
        self.btnEliminar = tk.Button(self.root, text="Eliminar hábito", state= tk.DISABLED, command= self.eliminar_habito_gui)
        self.btnEliminar.pack(side= tk.TOP, pady=5)

        #Creando el botón Deshacer completado
        self.btnDeshacer = tk.Button(self.root, text="Deshacer completado", state=tk.DISABLED, command= self.deshacer_completado_gui)
        self.btnDeshacer.pack(side= tk.TOP, pady=5)

        #Creando el botón Subir hábito
        self.btnSubir = tk.Button(self.root, text= "↑ Subir", state= tk.DISABLED, command= self.subir_habito_gui)
        self.btnSubir.pack(side= tk.TOP, pady=2)

        #Creando el botón Bajar hábito
        self.btnBajar = tk.Button(self.root, text= "↓ Bajar", state= tk.DISABLED, command= self.bajar_habito_gui)
        self.btnBajar.pack(side= tk.TOP, pady=2)


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
            self.listbox.see(tk.END) #Desplaza scrool al final
            self.listbox.selection_set(tk.END) #Se selecciona el nuevo hábito insertado
            self.habilitar_botones()
    
    def mostrar_mensaje(self, mensaje, estado):
        color = "green" if estado == "ok" else "red"
        self.lblMensaje.config(text= mensaje, fg= color)
        self.root.after(3000, lambda: self.lblMensaje.config(text=""))

    def actualizar_ListBox(self):
        self.listbox.delete(0, tk.END)
        self.listar_ListBox()
        self.listbox.yview_moveto(1) #Scroll autómatico, desplaza al final (1)
        

    def listar_ListBox(self):
        for habito in self.gestor.habitos:
            nombre = habito["nombre"]
            completado = "[X]" if habito['completado'] else "[ ]"
            self.listbox.insert(tk.END, f"{nombre}   -   {completado}")

    def completar_habito_gui(self):
        #Obtenemos el indice del habito seleccionado en el listbox
        indice = self.listbox.curselection() # Formato tupla: (indice,)
        if not indice:
            return #Evita error si no hay selección
        
        mensaje, estado = self.gestor.completar_habito(indice[0])
        self.mostrar_mensaje(mensaje, estado)

        if estado == "ok":
            self.actualizar_ListBox()
            self.listbox.selection_clear(0,tk.END) #Quitar selección del listbox
            self.habilitar_botones()
    
    def eliminar_habito_gui(self):
        #Obtenemos el indice del hábito seleccionado a eliminar
        indice = self.listbox.curselection() #Format tupla: (indice,)
        if not indice:
            return
        
        mensaje, estado = self.gestor.eliminar_habito(indice[0])
        self.mostrar_mensaje(mensaje,estado)

        if  estado == "ok":
            self.actualizar_ListBox()
            self.listbox.select_clear(0,tk.END)
            self.habilitar_botones()

    def deshacer_completado_gui(self):
        #Obtenemos el indice del hábito seleccionado
        indice = self.listbox.curselection()

        if not indice:
            return #Evita error si no hay selección
        
        mensaje, estado = self.gestor.deshacer_habito(indice[0])
        self.mostrar_mensaje(mensaje, estado)

        if(estado == "ok"):
            self.actualizar_ListBox()
            self.listbox.selection_clear(0,tk.END) #Quitar selección del inbox
            self.habilitar_botones()
    
    def subir_habito_gui(self):
        #Capturamos el índice del hábito seleccionado
        indice = self.listbox.curselection()[0]
        
        mensaje, estado = self.gestor.subir_habito(indice)
        self.mostrar_mensaje(mensaje, estado)

        if estado == "ok":
            self.actualizar_ListBox()
            self.listbox.select_clear(0,tk.END)
            self.habilitar_botones()


    def bajar_habito_gui(self):
        #Capturamos el índice del hábito seleccionado
        indice = self.listbox.curselection()[0]
        
        mensaje, estado = self.gestor.bajar_habito(indice)
        self.mostrar_mensaje(mensaje, estado)

        if estado == "ok":
            self.actualizar_ListBox()
            self.listbox.select_clear(0,tk.END)
            self.habilitar_botones()

        
    
    def habilitar_botones(self):

        #Comprobamos el número de hábitos guardados en el sistema
        longitud = len(self.gestor.habitos)
        #Capturamos el hábito seleccionado
        indice = self.listbox.curselection() #Formato tupla (2, )   
        
        if indice:

            #Botón Subir y bajar
            if longitud > 1:
                if indice[0] == 0: #Primer elemento de la lista
                    self.btnBajar.config(state= tk.NORMAL)
                    self.btnSubir.config(state= tk.DISABLED)
                elif indice[0] == longitud - 1: #Último elemento de la lista
                    self.btnSubir.config(state= tk.NORMAL)
                    self.btnBajar.config(state= tk.DISABLED)
                else:
                    self.btnSubir.config(state= tk.NORMAL)
                    self.btnBajar.config(state= tk.NORMAL)

            #Botón eliminar
            self.btnEliminar.config(state= tk.NORMAL)

            #Botón Completar y deshacer

            #Obtenemos el texto del habito seleccionado
            texto = self.listbox.get(indice[0])
            #Filtramos si esta o no completado
            completado = texto[-3:]

            if completado == "[ ]":
                self.btnCompletar.config(state= tk.NORMAL)
                self.btnDeshacer.config(state= tk.DISABLED)
            else:
                self.btnCompletar.config(state= tk.DISABLED)
                self.btnDeshacer.config(state= tk.NORMAL) 

        else:
            self.btnEliminar.config(state= tk.DISABLED)
            self.btnCompletar.config(state= tk.DISABLED)
            self.btnDeshacer.config(state= tk.DISABLED)
            self.btnSubir.config(state= tk.DISABLED)
            self.btnBajar.config(state= tk.DISABLED)


