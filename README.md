# 🧘 Gestor de Hábitos Diarios

Este proyecto es una evolución progresiva de un gestor de hábitos personales desarrollado en Python.  
Su objetivo es construir una herramienta funcional, profesional y mantenible, pasando por varias fases de aprendizaje y mejora.

---

## 📌 Objetivo

- Registrar hábitos diarios  
- Marcar hábitos como completados  
- Persistencia de datos entre sesiones  
- Aprender buenas prácticas de programación evolutiva  

---

## 🔁 Fases del proyecto

| Fase   | Descripción                                                  | Carpeta               |
|--------|--------------------------------------------------------------|------------------------|
| Fase 1 | Lógica completa en un solo archivo, con persistencia en JSON | `/v1_linea_a_linea`    |
| Fase 2 | Separación por funciones con persistencia                    | `/v2_funciones`        |
| Fase 3 | Versión con clases (OOP), más modular y escalable            | `/v3_clases`           |
| Fase 4 | Interfaz gráfica básica usando tkinter                       | `/v4_gui_tkinter`      |
| Fase 5 | Interfaz modular con mejoras internas y feedback visual      | `/v5_interfaz_modular` |

---

### 🧠 Detalle por fases

#### ✅ Fase 1 – Estructura mínima del proyecto
- Lógica funcional sin separación de responsabilidades.  
- Lectura/escritura de hábitos en JSON en el mismo archivo.

#### ✅ Fase 2 – Separación por funciones
- Código más limpio y organizado.  
- Persistencia separada en funciones reutilizables.

#### ✅ Fase 3 – Orientación a objetos
- Uso de clases para encapsular la lógica (`GestorDeHabitos`).  
- Proyecto preparado para escalar.

#### ✅ Fase 4 – Interfaz gráfica básica con tkinter
- Primer GUI con `Entry`, `Button` y `Listbox`.  
- Posibilidad de añadir y completar hábitos desde la interfaz.

#### ✅ Fase 5 – Interfaz modular y visual
- Métodos separados por zonas: entrada, lista y botones.  
- Etiqueta (`Label`) para mensajes temporales con color.  
- Scroll automático y selección del nuevo hábito.
- Botones que se activan o desactivan dinámicamente.
- Eliminar y deshacer hábitos desde la interfaz.  
- Reordenar hábitos con botones "↑" y "↓".

---

## 🗺️ Hoja de ruta del proyecto

Este proyecto se desarrolla en fases evolutivas, cada una con un enfoque progresivo de aprendizaje y profesionalización.

| Fase   | Zona     | Descripción                                                                 | Estado       |
|--------|----------|-----------------------------------------------------------------------------|--------------|
| Fase 1 | -        | Lógica básica en un solo archivo. Persistencia en JSON.                     | ✅ Finalizada |
| Fase 2 | -        | Modularización por funciones. Código más legible.                           | ✅ Finalizada |
| Fase 3 | -        | Programación orientada a objetos (POO). Proyecto más escalable.             | ✅ Finalizada |
| Fase 4 | -        | Interfaz gráfica básica con tkinter. Visualización y control en GUI.        | ✅ Finalizada |
| Fase 5 | Zona 1   | Refactor GUI: interfaz modular con zonas (`entrada`, `lista`, `botones`).   | ✅ Finalizada |
| Fase 5 | Zona 2   | Mejoras UX: scroll automático, feedback visual, selección, validaciones.    | ✅ Finalizada |
| Fase 5 | Zona 3   | Funcionalidad para eliminar hábitos desde la GUI.                           | ✅ Finalizada |
| Fase 5 | Zona 4   | Opción para desmarcar hábitos completados (estado "incompleto").            | ✅ Finalizada |
| Fase 5 | Zona 5   | Reordenar hábitos visualmente (botones).                                    | ✅ Finalizada |
| Fase 6 | -        | Rediseño visual completo y mejoras avanzadas de persistencia.               | 🕓 Futuro  |
| Fase 7 | -        | Exportación, estadísticas, integración con calendario, sincronización.      | 🕓 Futuro     |
| Fase 8 | -        | Gamificación: niveles, XP, hábitos estrella, recompensas simbólicas.        | 🕓 Futuro     |

---

## ▶️ Cómo ejecutar

```bash
cd v1_linea_a_linea
python habitos.py

cd v2_funciones
python habitos.py

cd v3_clases
python habitos.py

cd v4_gui_tkinter
python main.py

cd v5_interfaz_modular
python main.py

```

---

## 💻 Autor

Este proyecto forma parte del portafolio de [@jmunozw](https://github.com/jmunozw).

Desarrollado como parte de mi ruta hacia Dev profesional con ChatGPT como mentor técnico y la guía práctica de MoureDev.