import json, os

def guardar_habitos(habitos):
    with open("habitos.json","w",encoding="utf-8") as archivo:
        json.dump(habitos,archivo,ensure_ascii=False, indent=4)

def cargar_habitos():
    if os.path.exists("habitos.json"):
        with open("habitos.json","r",encoding="utf-8") as archivo:
            return json.load(archivo)
    else:
        return []


habitos = cargar_habitos()



while(True):

    print("----------- Ritual Diario -----------")
    print("1. Añadir hábito")
    print("2. Ver hábitos")
    print("3. Completar hábito")
    print("4. Salir")

    opcion = input("Elige una opción: ").strip()
    
    if opcion == "1":
        nuevoHabito = input("¿Qué hábito deseas añadir?: ").strip()

        if not nuevoHabito:
            print("No se puede añadir un habito en blanco")
        elif any(h["nombre"] == nuevoHabito for h in habitos):
            print(f"El hábito '{nuevoHabito}' ya existe.")
        else:
            habitos.append({"nombre": nuevoHabito, "completado": False})
            guardar_habitos(habitos)
            print(f"Hábito '{nuevoHabito}' añadido.")

    elif opcion == "2":
        if len(habitos) == 0:
            print("Aún no has añadido ningún hábito.")
        else:
            print("Tus hábitos:")
            for i,habito in enumerate(habitos,start=1):
                print(f"{i}. {habito['nombre']} {'[X]' if habito['completado'] else '[ ]'}")

    elif opcion == "3":

        if len(habitos) == 0:
            print("Aún no has añadido ningún hábito.")
        else:
            print("Tus hábitos:")
            for i,habito in enumerate(habitos,start=1):
                print(f"{i}. {habito['nombre']} {'[X]' if habito['completado'] else '[ ]'}")
            
            marcarHabito = input("¿Qué hábito deseas marcar como completado? (número): ").strip()

            if not marcarHabito.isdigit():
                print("Debes elegir el número de hábito")
            else:
                marcar = int(marcarHabito)
                if 1 <= marcar <= len(habitos):
                    habitos[marcar-1]["completado"] = True
                    guardar_habitos(habitos)
                    print(f"Hábito '{habitos[marcar-1]['nombre']} marcado como completado.")
                else:
                    print("Fuera de rango") 

    elif opcion == "4":
        print("Salir del programa")
        break
    else:
        print("Opción no válida.")
