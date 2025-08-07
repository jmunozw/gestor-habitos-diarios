import tkinter as tk
from tkinter import messagebox
from gestorHabitos import GestorDeHabitos


class InterfazHabitos:

    def __init__(self, root):
        
        #Nuestra ventana principal
        self.root = root
        self.root.title("Ritual diario")
        self.root.geometry("450x450")
        self.root.minsize(400,300)
        self.root.configure(bg="#f0f0f0")
        

        #Intanciamos gestor
        self.gestor = GestorDeHabitos()

        #Construimos nuestra interfaz.
        self.construirInterfaz()

    def construirInterfaz(self):

        self.crear_zona_entrada()
        self.crear_zona_lista()
        self.crear_zona_botones()

        # Insertamos todos los habitos cargados desde el gestorDeHabitos
        self.listar_ListBox()
    
    def crear_zona_entrada(self):

        #Frame principal
        self.frame_superior = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_superior.pack(fill="x")
        
        #Frame para texto y botón añadir
        self.frame_anadir_habito = tk.Frame(self.frame_superior)
        self.frame_anadir_habito.pack(side= tk.TOP, pady=10)

        # Creando el campo de entrada de texto
        self.placeholder = "Escribe un nuevo hábito..."
        self.txtHabito = tk.Entry(self.frame_anadir_habito, fg="gray", width=25)
        self.txtHabito.pack(side=tk.LEFT, padx=15, pady=5)
        self.txtHabito.insert(0, self.placeholder)
        self.txtHabito.bind("<Return>", lambda event: self.añadir_habito_gui()) #Permitir añadir hábito con la tecla Enter
        self.txtHabito.bind("<FocusIn>", self._placeholder_focus_in)
        self.txtHabito.bind("<FocusOut>", self._placeholder_focus_out)

        # Creando el botón Añadir habito
        self.btnAñadir = tk.Button(self.frame_anadir_habito, text="Añadir hábito", relief="groove", command= self.añadir_habito_gui)
        self.btnAñadir.pack(side=tk.LEFT, padx= 15, pady=5)

        #Creando label de mensaje
        self.lblMensaje = tk.Label(self.frame_superior, text= "", font=("Arial",9,"italic"), fg="green", bg="#f0f0f0")
        self.lblMensaje.pack(side= tk.BOTTOM, pady=(2,5))

    def crear_zona_lista(self):

        #Creamos un frame central
        self.frame_central = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_central.pack(fill="x", pady=5)

        #Creamos frame contenedor
        self.frame_agrupado = tk.Frame(self.frame_central, relief="groove", bd=2, bg="#f0f0f0", padx=10, pady=10)
        self.frame_agrupado.pack(pady=5)
        self.root.update_idletasks() # Asegura que tkinter calcule bien los tamaños.
        self.ancho_frame_agrupado = self.frame_agrupado.winfo_width()

        #Creamos el frame donde colocaremos el titurlo, la lista, el scroll y los botones de subir y bajar 
        self.frame_lista_mover = tk.Frame(self.frame_agrupado, bg="#f0f0f0")
        self.frame_lista_mover.pack(padx=10)

        #Creamos Titulo para la lista de hábitos
        self.lblTituloLista = tk.Label(self.frame_lista_mover, text="📋Tus hábitos diarios", bg="#f0f0f0", font=("Arial",10,"bold"))
        self.lblTituloLista.pack(side= tk.TOP)
        
        #Creamos otro frame que contendra la lista y el scrollbar por si lo necesite
        self.frame_lista_con_scroll = tk.Frame(self.frame_lista_mover, bd=2, bg="#f0f0f0")
        self.frame_lista_con_scroll.pack(side= tk.LEFT, padx=10, pady=10)

        #Scrollbar
        scrollbar = tk.Scrollbar(self.frame_lista_con_scroll, orient= tk.VERTICAL)
        scrollbar.pack(side= tk.RIGHT, fill= tk.Y)

        # Creamos un Listbox para visualizar los hábitos
        self.listbox = tk.Listbox(self.frame_lista_con_scroll, width=44, height=7, highlightthickness=0, yscrollcommand= scrollbar.set)
        self.listbox.pack(side=tk.LEFT)

        #Otra frame donde colocaremos los botones. Este estara dentro del frame_lista_mover
        self.frame_mover = tk.Frame(self.frame_lista_mover, bg="#f0f0f0")
        self.frame_mover.pack(side= tk.RIGHT, anchor="n",padx=10, pady=30)

        #Creando el botón Subir hábito
        self.btnSubir = tk.Button(self.frame_mover, text= "↑ Subir", width=6, relief="groove", state= tk.DISABLED, command= self.subir_habito_gui)
        self.btnSubir.pack(pady=5)

        #Creando el botón Bajar hábito
        self.btnBajar = tk.Button(self.frame_mover , text= "↓ Bajar", width=6, relief="groove", state= tk.DISABLED, command= self.bajar_habito_gui)
        self.btnBajar.pack(pady=5)

        # Vinculando evento listbox y los botones completar y eliminar
        self.listbox.bind("<<ListboxSelect>>", lambda event: self.habilitar_botones())

    def crear_zona_botones(self):

        #Creamos el frame contenedor
        self.frame_acciones_grupo = tk.LabelFrame(self.root, text="Acciones rápidas", font=("Arial",9,"bold"), fg="#333", labelanchor="n",bd=2, bg="#f0f0f0", padx=5, pady=5)
        self.frame_acciones_grupo.pack(anchor="center", pady=10)

        #Creamos el frame donde colocaremos los botones
        self.frame_acciones = tk.Frame(self.frame_acciones_grupo, bg="#f0f0f0")
        self.frame_acciones.pack(padx=5, pady=5)

        # Creando el botón Completar hábito
        self.btnCompletar = tk.Button(self.frame_acciones,text="Completar\nhábito", relief="groove", width=12, state = tk.DISABLED, command= self.completar_habito_gui)
        self.btnCompletar.pack(side=tk.LEFT, padx=5, pady=5)

        #Creando el botón Eliminar hábito
        self.btnEliminar = tk.Button(self.frame_acciones, text="Eliminar\nhábito", relief="groove", width=12, state= tk.DISABLED, command= self.eliminar_habito_gui)
        self.btnEliminar.pack(side= tk.LEFT, padx=5, pady=5)

        #Creando el botón Deshacer completado
        self.btnDeshacer = tk.Button(self.frame_acciones, text="Deshacer\ncompletado", relief="groove", width=12, state=tk.DISABLED, command= self.deshacer_completado_gui)
        self.btnDeshacer.pack(side= tk.LEFT, padx=5, pady=5)

        #Creando el botón Resetear hábitos
        self.btnResetear = tk.Button(self.frame_acciones, text="Resetear\ntodos", relief="groove", width=12, command= self.resetear_todos_gui)
        self.btnResetear.pack(side= tk.LEFT, padx=5, pady=5)

    def _placeholder_focus_in(self, event):
        if(self.txtHabito.get() == self.placeholder):
            self.txtHabito.delete(0, tk.END)
            self.txtHabito.config(fg= "black")

    def _placeholder_focus_out(self, event):
        if not self.txtHabito.get(): 
            self.txtHabito.insert(0, self.placeholder)
            self.txtHabito.config(fg="gray")


    def añadir_habito_gui(self):
        nuevoHabito =  self.txtHabito.get()
        
        #Controlamos que no se acepte como hábito el placeholder o un texto vacio
        if nuevoHabito == self.placeholder or not nuevoHabito.strip():
            self.mostrar_mensaje("Escribe un nuevo hábito válido", "error")
            return
        
        mensaje, estado = self.gestor.añadir_habitos(nuevoHabito)

        self.mostrar_mensaje(mensaje,estado)

        if estado == "ok":
            self.txtHabito.delete(0, tk.END)
            self.actualizar_ListBox()
            self.listbox.see(tk.END) #Desplaza scrool al final
            self.listbox.selection_set(tk.END) #Se selecciona el nuevo hábito insertado
            self.habilitar_botones()
        
        #Una vez finalizado el añadir habito, enfocamos nuevamente el txt para seguir escribiendo
        self.txtHabito.focus_set()
    
    def mostrar_mensaje(self, mensaje, estado):
        color = "green" if estado == "ok" else "red"
        self.lblMensaje.config(text= mensaje, fg= color)
        self.root.after(3000, lambda: self.lblMensaje.config(text=""))

    def actualizar_ListBox(self):
        self.listbox.delete(0, tk.END)
        self.listar_ListBox()
        self.listbox.yview_moveto(1) #Scroll autómatico, desplaza al final (1)
        

    def listar_ListBox(self):
        self.listbox.delete(0, tk.END) #Limpiamos el listbox

        for idx, habito in enumerate(self.gestor.habitos):
            nombre = habito["nombre"]
            completado = "[X]" if habito['completado'] else "[ ]"
            self.listbox.insert(tk.END, f"{nombre}   -   {completado}")

            #Diferenciamos visualmente los completados
            if habito["completado"]:
                self.listbox.itemconfig(idx, fg= "gray")
            else:
                self.listbox.itemconfig(idx, fg= "black")

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
        
        #Obtenemos el nombre del hábito
        nombre_habito = self.gestor.habitos[indice[0]]['nombre']
        
        #POPUP de confirmación
        confirmar = messagebox.askyesno("Confirmar eliminación", f"¿Seguro que quieres eliminar el hábito:\n\n'{nombre_habito}'?")

        if confirmar:
            mensaje, estado = self.gestor.eliminar_habito(indice[0])
            self.mostrar_mensaje(mensaje,estado)

            if  estado == "ok":
                self.actualizar_ListBox()
                self.listbox.select_clear(0,tk.END)
                self.habilitar_botones()
        else:
            return

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

    def resetear_todos_gui(self):
        if not self.gestor.habitos:
            self.mostrar_mensaje("No hay hábitos para resetear","error")
            return
        confirmar = messagebox.askyesno("Confirmar reseteo","¿Seguro que quieres resetear TODOS los hábitos a no completados?")

        if confirmar:
            mensaje, error = self.gestor.resetear_habitos()
            self.mostrar_mensaje(mensaje, error)
            self.actualizar_ListBox()
        else:
            self.mostrar_mensaje("Reseteo cancelado","error")
    
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
        


