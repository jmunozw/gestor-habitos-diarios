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
            print("No se puede añadir un habito en blanco")
        elif any(h["nombre"] == nuevoHabito for h in self.habitos):
            print(f"El hábito '{nuevoHabito}' ya existe.")
        else:
            self.habitos.append({"nombre": nuevoHabito, "completado": False})
            self.guardar_habitos()
            print(f"Hábito '{nuevoHabito}' añadido.")

    def ver_habitos(self):
        if len(self.habitos) == 0:
            print("Aún no has añadido ningún hábito.")
        else:
            print("Tus hábitos:")
            for i,habito in enumerate(self.habitos, start=1):
                print(f"{i}. {habito['nombre']}  {'[X]' if habito['completado'] else '[ ]'}")
    
    def completar_habito(self, indice):
        if not self.habitos:
            print("Aún no has añadido ningún hábito.")
            return
    
        self.habitos[indice]["completado"] = True
        self.guardar_habitos()
        print(f"Hábito '{self.habitos[indice]['nombre']}' marcado como completado.")