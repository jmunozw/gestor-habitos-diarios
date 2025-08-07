# 🧘 Ritual Diario – Versión 6

Gestor gráfico de hábitos diarios en Python con interfaz desarrollada en `tkinter`.  
Permite añadir, completar, deshacer, eliminar, reordenar y resetear hábitos, con persistencia en JSON.

---

## 🚀 Características principales

- ✅ Añadir hábitos con validación
- 🔄 Completar / deshacer hábitos
- 🗑️ Eliminar hábitos
- 🔼🔽 Reordenar hábitos con botones
- ♻️ Resetear todos los hábitos a estado no completado
- 💾 Persistencia automática con archivo `habitos.json`
- 💬 Mensajes emergentes de confirmación y feedback visual
- ⌨️ Soporte para añadir hábitos con tecla `Enter`
- 🧠 Entrada con *placeholder* y autoenfoque
- 🔲 Interfaz compacta y ordenada en módulos

---

## 📂 Estructura del proyecto

ritual_diario_v6/
├── main.py # Arranque principal de la app
├── interfaz.py # Interfaz gráfica con tkinter
├── gestorHabitos.py # Lógica de gestión de hábitos
├── habitos.json # Archivo con los hábitos almacenados
└── README.md # Este archivo


---

## 🧩 Tecnologías utilizadas

- **Python 3.x**
- **Tkinter** (estándar de Python)
- **JSON** para almacenamiento local

---

## 📚 Aprendizaje progresivo

Este proyecto forma parte de un proceso de aprendizaje **por versiones**, desde un script lineal hasta esta versión modular y presentable.

👉 Esta versión (`v6`) representa el primer **rediseño profesional** del proyecto.  
Se centra en buenas prácticas, legibilidad del código, separación de responsabilidades y persistencia de datos.

---

## 🧠 Autor

**Jorge Muñoz Wunder**  
GitHub: [@jmunozw](https://github.com/jmunozw)

---

## 📌 Notas

- Se ha evitado usar librerías externas para maximizar el aprendizaje de Python puro y `tkinter`.
- Próximas versiones podrían usar `ttk` para mejorar diseño visual o añadir funcionalidades como estadísticas.
