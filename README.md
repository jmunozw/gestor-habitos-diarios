# 🧘 Gestor de Hábitos Diarios

Este proyecto es una evolución progresiva de un gestor de hábitos personales desarrollado en Python.  
Su objetivo es construir una herramienta funcional, profesional y mantenible, pasando por varias fases de aprendizaje y mejora.

---

## 📌 Objetivo

- Registrar hábitos diarios  
- Marcar hábitos como completados  
- Persistencia de datos entre sesiones  
- Aprender buenas prácticas de programación evolutiva  
- Diseñar una interfaz gráfica modular y presentable para portafolio

---

## 🔁 Fases del proyecto

| Fase   | Descripción                                                  | Carpeta               |
|--------|--------------------------------------------------------------|------------------------|
| Fase 1 | Lógica completa en un solo archivo, con persistencia en JSON | `/v1_linea_a_linea`    |
| Fase 2 | Separación por funciones con persistencia                    | `/v2_funciones`        |
| Fase 3 | Versión con clases (OOP), más modular y escalable            | `/v3_clases`           |
| Fase 4 | Interfaz gráfica básica usando tkinter                       | `/v4_gui_tkinter`      |
| Fase 5 | Interfaz modular con mejoras internas y feedback visual      | `/v5_interfaz_modular` |
| Fase 6 | Rediseño profesional, pulido visual y presentación final     | `/v6_rediseño_profesional` |

---

## 🧠 Detalle por fases

#### ✅ Fase 1 – Estructura mínima
- Toda la lógica en un solo archivo.
- Lectura/escritura JSON básica.

#### ✅ Fase 2 – Modularización por funciones
- Código más limpio y legible.
- Reutilización de funciones.

#### ✅ Fase 3 – Orientación a objetos
- Encapsulamiento de la lógica.
- Clase `GestorDeHabitos`.

#### ✅ Fase 4 – GUI con tkinter
- Entrada, botón y lista de hábitos.
- Añadir y completar hábitos.

#### ✅ Fase 5 – Interfaz modular
- Separación de zonas (entrada, lista, botones).
- Feedback visual, scroll automático, selección dinámica.
- Eliminar, deshacer y reordenar hábitos.

#### ✅ Fase 6 – Rediseño profesional
- Código dividido en módulos (`main`, `gestor`, `interfaz`).
- Diseño más ordenado, visual y funcional.
- Persistencia automática.
- Botón reset con popup de confirmación.
- Preparado como proyecto de portafolio.

---

## 🗺️ Hoja de ruta

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
| Fase 6 | -        | Rediseño visual, modularización, botones mejorados, persistencia y popup.   | ✅ Finalizada |
| Fase 7 | -        | Exportar hábitos, estadísticas, integración con calendario.                 | 🕓 Futuro     |
| Fase 8 | -        | Gamificación: niveles, XP, recompensas simbólicas.                          | 🕓 Futuro     |

---

## ▶️ Cómo ejecutar

```bash
# Ejemplos por carpeta:

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

cd v6_rediseño_profesional
python main.py


```

---

## 💻 Autor

Este proyecto forma parte del portafolio de [@jmunozw](https://github.com/jmunozw).

Desarrollado como parte de mi ruta hacia Dev profesional con ChatGPT como mentor técnico y la guía práctica de MoureDev.