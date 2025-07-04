import tkinter as tk
from gestorHabitos import GestorDeHabitos


def añadir_habito_gui():
    nuevoHabito = entry.get()
    gestor.añadir_habitos(nuevoHabito)
    entry.delete(0,tk.END)
    actualizar_ListBox()

def actualizar_ListBox():
    listbox.delete(0, tk.END)
    listar_ListBox()

def listar_ListBox():
    for habito in gestor.habitos:
        nombre = habito["nombre"]
        completado = "[X]" if habito['completado'] else "[ ]"
        listbox.insert(tk.END, f"{nombre}   -   {completado}")

def completar_habito_gui():
    #Obtenemos el indice del habito seleccionado en el listbox
    indice = listbox.curselection() # Formato tupla: (indice,)
    gestor.completar_habito(indice[0])
    actualizar_ListBox()
    
    

def habilitar_btnCompletar():
    if listbox.curselection():
        btnCompletar.config(state= tk.NORMAL)
    else:
        btnCompletar.config(state= tk.DISABLED)

# Ventana principal Ritual Diario
root = tk.Tk()
root.title("Ritual diario")

#Intanciamos gestor
gestor = GestorDeHabitos()

# Creando un Frame
my_frame = tk.Frame(root, width=200, height=210, bg="lightgray")
my_frame.pack()

# Creando el campo de entrada de texto
entry = tk.Entry(my_frame)
entry.pack(side=tk.LEFT, padx=15)

# Creando el botón Añadir habito
btnAñadir = tk.Button(my_frame,text="Añadir hábito", command= añadir_habito_gui)
btnAñadir.pack(side=tk.LEFT, padx= 15)

# Creando el botón Completar hábito
btnCompletar = tk.Button(root,text="Completar hábito", state = tk.DISABLED, command= completar_habito_gui)
btnCompletar.pack(side=tk.BOTTOM,pady=5)


# Creamos un Listbox para visualizar los hábitos
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Vinculando evento listbox y boton
listbox.bind("<<ListboxSelect>>", lambda event: habilitar_btnCompletar())

# Insertamos todos los habitos cargados desde el gestorDeHabitos
listar_ListBox()


# Iniciando el bucle principal de la interfaz
root.mainloop()