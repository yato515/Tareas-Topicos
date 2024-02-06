import tkinter as tk

ventana = tk.Tk() #creamos el objeto ventana
ventana.title("Ventana")
ventana.geometry("385x160+400+50") #el 450 y el 50 es para saber la pocision de la ventana
#ventana.resizable(width=False, height=False) #para no poder mover la ventana ni el tamaño

#Botones

boton1 = tk.Button(ventana, text= "Boton 1", width=7, relief="groove", font=("Book Antiqua",12,"bold")) 
boton1.place(x= 2, y=120)

boton2 = tk.Button(ventana, text= "Boton 2", width=7, relief="groove", font=("Book Antiqua",12,"bold")) 
boton2.place(x= 80, y=120)

boton3 = tk.Button(ventana, text= "Boton 3", width=7, relief="groove", font=("Book Antiqua",12,"bold")) 
boton3.place(x= 155, y=120)

boton4 = tk.Button(ventana, text= "Boton 4", width=7, relief="groove", font=("Book Antiqua",12,"bold")) 
boton4.place(x= 230, y=120)
boton5 = tk.Button(ventana, text= "Boton 5", width=7, relief="groove", font=("Book Antiqua",12,"bold")) 
boton5.place(x= 305, y=120)
ventana.mainloop() #con esto corremo la ventana