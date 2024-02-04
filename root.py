import tkinter as tk

#colores
fondo_entrar = "#38B6FF"
fondo_salir = "#FFFFFF"
fondo_correcto = "#00BF63"
fondo_incorrecto = "#C40404"
fondo_entrada = "#FFFFFF"

#root quiere decir ventana, podemos ponerle el nombre que queramos
root = tk.Tk()
root.title("Login")
root.geometry("400x400+450+50")
root.resizable(width=False, height=False) #evita que los botones se muevan
fondo = tk.PhotoImage(file="Usuario.png")
fondo1 = tk.Label(root, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

usuario = tk.StringVar()
contraseña = tk.StringVar()
 
#Entrada
entrada = tk.Entry(root, textvar= usuario, width= 22, relief= "flat", bg=fondo_entrada)
entrada.place(x=220 ,y=150 ) 

entrada1 = tk.Entry(root, textvar= contraseña, width= 22, relief= "flat", bg=fondo_entrada)
entrada1.place(x=220 ,y=210 ) 

def salir():
    root.destroy()

def correcta():

    root.withdraw()
    ventana1 = tk.Toplevel()
    ventana1.title("Ingresaste")
    ventana1.geometry("400x400+450+50")
    ventana1.resizable(width=False, height=False) #evita que los botones se muevan
    fondo2 = tk.PhotoImage(file="correcto.png")
    fondo2 = tk.Label(root, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

def login():
    nombre = usuario.get()
    pasword = contraseña.get()
    if nombre == "Humberto" and pasword == "amayagod":
        correcta()
    else: 
        incorrecta()



#Botones
boton = tk.Button(root, text="Entrar", cursor="hand2", bg=fondo_entrar, width=10, relief="flat",
                 font=("Book Antiqua",12,"bold"))
boton.place(x=33, y=296.5)

boton1 = boton = tk.Button(root, text="Salir",command=salir ,cursor="hand2", bg=fondo_salir, width=10, relief="flat",
                 font=("Book Antiqua",12,"bold"))
boton1 = boton.place(x=219, y=298)

root.mainloop() #con esto corremos la ventana
