# 🚀 Fase 5 – Interfaz modular con mejoras internas

En esta fase del proyecto **Gestor de Hábitos Diarios**, se mejora la estructura del código con foco en limpieza, escalabilidad y experiencia de usuario.

---

## 🎯 Objetivos

- Modularizar la interfaz gráfica dividiendo su construcción en zonas específicas.
- Preparar la clase `InterfazHabitos` para futuras ampliaciones.
- Añadir feedback visual mediante mensajes temporales.
- Aplicar buenas prácticas de legibilidad y mantenimiento.

---

## 🧩 Mejoras implementadas

- Clase `InterfazHabitos` dividida en métodos:
  - `crear_zona_entrada()`
  - `crear_zona_lista()`
  - `crear_zona_botones()`
- Método `mostrar_mensaje()` para centralizar la lógica de feedback.
- Validación de:
  - Campos en blanco.
  - Hábitos duplicados.
- Etiqueta de mensaje dinámico (`Label`) con colores:
  - Verde para éxito (`ok`)
  - Rojo para error (`error`)
- Scroll automático al final del `Listbox` al añadir un nuevo hábito.
- Selección automática del nuevo hábito tras añadirlo.
- Botón "Completar hábito" se desactiva automáticamente tras completarlo.
- Prevención de errores si se pulsa "Completar hábito" sin selección previa.
- Código limpio, visualmente estructurado y reutilizable.


---

## 📂 Archivos principales

- `interfaz.py` → Interfaz gráfica modular (Tkinter)
- `gestorHabitos.py` → Lógica del gestor y persistencia en JSON
- `habitos.json` → Archivo de almacenamiento de hábitos

---

## ▶️ Ejecutar

```bash
python main.py

```