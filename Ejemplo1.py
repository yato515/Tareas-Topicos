import tkinter as tk

# colores
fond_botonE = "#38B6FF"
fondo_entrada = "#B5B2B2"
fondo_ventana = "#9FFCFD"
fondo_frame = "#000000"

# Ventana

ventana = tk.Tk()
frame = tk.Frame()
ventana.title("Pantalla 1")
ventana.geometry("385x160+400+50")
ventana.config(bg=fondo_ventana)
ventana.iconbitmap("dragon.ico")

# Métodos
entrada = tk.StringVar()
entrada2 = tk.StringVar()

def correcta():
    ventana.withdraw()
    ventana1 = tk.Toplevel()
    ventana1.title("Ingresaste")
    ventana1.geometry("400x400+450+50")
    ventana1.config(bg=fondo_ventana)
    ventana1.iconbitmap("dragon.ico")

def login():
    nombre = entrada.get()
    pasword = entrada2.get()
    if nombre == "humberto" and pasword == "yato":
        
        correcta()

# Texto

texto = tk.Label(ventana, text="Nombre", font=("Book Antiqua", 12, "bold"), bg=fondo_frame, fg="white")
texto.pack()
texto.place(x=50, y=15)

contra = tk.Label(ventana, text="Contraseña", font=("Book Antiqua", 12, "bold"), bg=fondo_frame, fg="white")
contra.pack()
contra.place(x=45, y=65)

# Frame

frame.pack()
frame.config(bg=fondo_frame)
frame.config(width="385", height="160")

# Entrada

entrada = tk.Entry(ventana, width=35, relief="flat", bg=fondo_entrada)
entrada.place(x=140, y=17)
entrada2 = tk.Entry(ventana, width=35, relief="flat", bg=fondo_entrada)
entrada2.place(x=140, y=65)
entrada2.config(show="*")

# Botones

boton1 = tk.Button(ventana, text="Boton 1", width=7, relief="groove", font=("Book Antiqua", 12), bg=fond_botonE,
                   cursor="pirate", command=login)
boton1.place(x=150, y=120)
boton1.bind("<Return>", (lambda event: login()))

ventana.mainloop()
