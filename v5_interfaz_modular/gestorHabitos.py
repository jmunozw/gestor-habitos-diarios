import os, json

class GestorDeHabitos:

    def __init__(self):
        self.habitos = self.cargar_habitos()
    
    def cargar_habitos(self):
        if os.path.exists("habitos.json"):
            with open("habitos.json","r",encoding="utf-8") as archivo:
                return json.load(archivo)
        else:
            return []

    def guardar_habitos(self):
        with open("habitos.json","w",encoding="utf-8") as archivo:
            json.dump(self.habitos, archivo, ensure_ascii= False, indent=4)

    def añadir_habitos(self,nuevoHabito):
        
        if not nuevoHabito:
            return "No se puede añadir un habito en blanco","error"
        
        if any(h["nombre"] == nuevoHabito for h in self.habitos):
            return f"El hábito '{nuevoHabito}' ya existe.", "error"
        
        self.habitos.append({"nombre": nuevoHabito, "completado": False})
        self.guardar_habitos()
        return f"Hábito '{nuevoHabito}' añadido.","ok"

    def ver_habitos(self):
        if len(self.habitos) == 0:
            print("Aún no has añadido ningún hábito.")
        else:
            print("Tus hábitos:")
            for i,habito in enumerate(self.habitos, start=1):
                print(f"{i}. {habito['nombre']}  {'[X]' if habito['completado'] else '[ ]'}")
    
    def completar_habito(self, indice):
        if not self.habitos:
            return "Aún no has añadido ningún hábito.", "error"
    
        self.habitos[indice]["completado"] = True
        self.guardar_habitos()
        return f"Hábito '{self.habitos[indice]['nombre']}' marcado como completado.","ok"
    
    def deshacer_habito(self, indice):
        if not self.habitos:
            return "Aún no has añadido ningún hábito.", "error"
    
        self.habitos[indice]["completado"] = False
        self.guardar_habitos()
        return f"Hábito '{self.habitos[indice]['nombre']}' marcado como no completado.","ok"
    
    def eliminar_habito(self, indice):
        if not self.habitos:
            return "Aún no has añadido ningún hábito.", "error"
        habito = self.habitos[indice]["nombre"]

        del self.habitos[indice]
        self.guardar_habitos()
        return f"Hábito {habito} eliminado correctamente.", "ok"