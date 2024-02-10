import tkinter as tk

#colores
fond_botonE = "#38B6FF"
fondo_entrada = "#B5B2B2"
fondo_ventana = "#9FFCFD"
fondo_frame = "#000000"

#Ventana

ventana = tk.Tk()
frame =tk.Frame()
ventana.title("Pantalla 1")
ventana.geometry("385x160+400+50") #el 450 y el 50 es para saber la pocision de la ventana
#ventana.resizable(width=False, height=False)
ventana.config( bg= fondo_ventana )
ventana.iconbitmap("dragon.ico") #cambiamos el icono 


#Texto

texto = tk.Label(ventana, text="Nombre",font=("Book Antiqua",12,"bold"), bg= fondo_frame, fg="white" ) #confi del texto
texto.pack()
texto.place(x=45,y=50) #ubicacion del texto

#Frame

frame.pack()
frame.config(bg=fondo_frame) #se le da color al frame
frame.config(width="385", height="160")#y sus medidas 

#ENTRADA

entrada = tk.Entry(ventana,width= 35, relief= "flat", bg= fondo_entrada)
entrada.place(x=120 ,y=55 ) 

#BOTONES

boton1 = tk.Button(ventana, text= "Boton 1", width=7, relief="groove", font=("Book Antiqua",12), bg= fond_botonE, cursor= "pirate") 
boton1.place(x= 150, y=120)

ventana.mainloop() #con esto corremo la ventana