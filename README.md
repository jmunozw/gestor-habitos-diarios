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

| Fase | Descripción | Carpeta |
|------|-------------|---------|
| Fase 1 | Lógica completa en un solo archivo, con persistencia en JSON | `/v1_linea_a_linea` |
| Fase 2 | Separación por funciones con persistencia | `/v2_funciones` |
| Fase 3 | Versión con clases (OOP), más modular y escalable | `/v3_clases` |
| Fase 4 | Interfaz gráfica básica usando tkinter | `/v4_gui_tkinter` |
| Fase 5 | Interfaz modular con mejoras internas y feedback visual | `/v5_interfaz_modular` |

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
- Preparación para próximas mejoras visuales y estructurales.

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