import tkinter as tk

ventana = tk.Tk()
ventana.title("Pantalla 1")
ventana.geometry("385x160+400+50") #el 450 y el 50 es para saber la pocision de la ventana
#ventana.resizable(width=False, height=False)

#ENTRADA

entrada = tk.Entry(ventana,width= 35, relief= "flat")
entrada.place(x=120 ,y=50 ) 
boton1 = tk.Button(ventana, text= "Boton 1", width=7, relief="groove", font=("Book Antiqua",12,"bold")) 
boton1.place(x= 150, y=120)

ventana.mainloop() #con esto corremo la ventana