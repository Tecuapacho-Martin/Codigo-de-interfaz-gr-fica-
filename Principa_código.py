import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Función para limpiar el área dinámica
def limpiar_area_dinamica():
    for widget in area_dinamica.winfo_children():
        widget.destroy()

# Función para la pantalla de inicio
def mostrar_pantalla_inicio():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Aquí va un mensaje de bienvenida", font=("Arial", 14)).pack(pady=10)
    tk.Button(area_dinamica, text="Mostrar mensaje de bienvenida", command=lambda: messagebox.showinfo("Título", "Mensaje temporal")).pack()

# Función para el formulario del alumno
def mostrar_formulario_alumno():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Aquí coloca un letrero o label que identifique al alumno", font=("Arial", 14)).pack(pady=10)

    tk.Label(area_dinamica, text="Nombre de el alumno:").pack()
    campo_texto_uno = tk.Entry(area_dinamica)
    campo_texto_uno.pack(pady=5)

    tk.Label(area_dinamica, text="Selección A:").pack()
    opcion_elegida = tk.StringVar(value="Opción 1")
    tk.Radiobutton(area_dinamica, text="Opción 1", variable=opcion_elegida, value="Opción 1").pack()
    tk.Radiobutton(area_dinamica, text="Opción 2", variable=opcion_elegida, value="Opción 2").pack()

    tk.Label(area_dinamica, text="Lista desplegable:").pack()
    combo = ttk.Combobox(area_dinamica, values=["Uno", "Dos", "Tres"])
    combo.pack()
    combo.current(0)

    def guardar_datos_alumno():
        valor = campo_texto_uno.get()
        messagebox.showinfo("Revisión", f"Texto: {valor}\nSelección: {opcion_elegida.get()}\nLista: {combo.get()}")

    tk.Button(area_dinamica, text="Guardar Datos", command=guardar_datos_alumno).pack(pady=10)

# Función para la configuración de la interfaz
def mostrar_configuracion_interfaz():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Configuraciones temporales", font=("Arial", 14)).pack(pady=10)

    colores = ["lightblue", "lightgreen", "lightyellow", "lightgray"]
    tk.Label(area_dinamica, text="Cambiar fondo:").pack()

    def cambiar_color_fondo(c):
        ventana_principal.config(bg=c)
        menu_lateral.config(bg=c)
        area_dinamica.config(bg=c)

    for c in colores:
        tk.Button(area_dinamica, text=c, bg=c, width=20, command=lambda col=c: cambiar_color_fondo(col)).pack(pady=2)

# Función para mostrar la pantalla de ayuda
def mostrar_pantalla_ayuda():
    limpiar_area_dinamica()
    tk.Label(area_dinamica, text="Texto de ayuda que el alumno debe mejorar", font=("Arial", 14)).pack(pady=10)
    contenido = (
        "Explica con tus palabras:\n\n"
        "- ¿Qué hace cada botón?\n"
        "- ¿Qué cambias si modificas un texto?\n"
        "- ¿Cómo cambias un color?\n"
        "- ¿Qué debes renombrar?"
    )
    tk.Label(area_dinamica, text=contenido, justify="left").pack(pady=10)

# Creación de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Interfaz para practicas")
ventana_principal.geometry("500x400")
ventana_principal.config(bg="lightblue")

# Creación del menú al lado
menu_lateral = tk.Frame(ventana_principal, bg="lightblue", width=120)
menu_lateral.pack(side="left", fill="y")

# Creación del área dinámica
area_dinamica = tk.Frame(ventana_principal, bg="white")
area_dinamica.pack(side="right", expand=True, fill="both")

# Botones del menú con las funciones actualizadas
tk.Button(menu_lateral, text="Inicio", command=mostrar_pantalla_inicio, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Formulario Alumno", command=mostrar_formulario_alumno, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Configuración", command=mostrar_configuracion_interfaz, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Ayuda", command=mostrar_pantalla_ayuda, width=15).pack(pady=10)
tk.Button(menu_lateral, text="Salir", command=ventana_principal.destroy, width=15).pack(pady=30)

# Mostrar pantalla de inicio 
mostrar_pantalla_inicio()

# Iniciar el bucle de la interfaz
ventana_principal.mainloop()
