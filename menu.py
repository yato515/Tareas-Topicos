import tkinter as tk
from tkinter import *

#COLORES
fondo_ventana = "#7092BE"
fondo_frame = "#000000"
fond_botonE = "#38B6FF"
fondo_entrada = "#B5B2B2"

ventana = tk.Tk()
ventana.title("Pantalla 1")
ventana.geometry("385x570+400+50")
#ventana.config()

my_list=['Futbol', 'Voleyball', 'Basquet', 'Box']
my_list2=['Lunes', 'Martes', 'miercoles','jueves','viernes']
my_list3=['mexico','brazil','argentina']
entrada = tk.StringVar()
nombre = entrada.get()
sexboton = tk.StringVar()
sexo = sexboton.set('hom')
sexo = sexboton.get()
disboton = tk.StringVar()
distancia = disboton.set('aas')
distancia = disboton.get()
cateboton = tk.StringVar()
cateboton.set(my_list[0])
categoria = cateboton.get()
entreno_boton = tk.StringVar()
entreno_boton.set(my_list2[0])
entreno = entreno_boton.get()
pais_boton = tk.StringVar()
pais_boton.set(my_list3[0])




#metodos
def login():
    nombre = entrada.get()
    sexo = sexboton.get()
    distancia = disboton.get()
    categoria = catego.get(tk.ACTIVE)  # Obtener el elemento seleccionado en la lista
    cateboton.set(categoria)  # Actualizar el valor de cateboton
    entreno = Dentreno.get(tk.ACTIVE)  # Obtener el elemento seleccionado en la lista
    entreno_boton.set(entreno)
    pais = pais_boton.get()
    pais_boton.set(pais)
    print(pais)
  
    ventana.withdraw()
    ventana1 = tk.Toplevel()
    ventana1.title("Ingresaste")
    ventana1.geometry("300x350+450+50")
    ventana1.config(bg=fondo_ventana)
    
    texto1 = tk.Label(ventana1, text='Nombre:', font=("Book Antiqua", 12, "bold"), bg= fondo_ventana, fg= 'black')
    texto1.pack()
    texto1.place(x=50, y=15)

    texto = tk.Label(ventana1, text='', font=("Book Antiqua", 12, "bold"), bg=fondo_entrada, fg="Black", relief='flat', width=12)
    texto.pack()
    texto.place(x=150, y=15)
    texto.config(text=nombre)

    texto_sexo = tk.Label(ventana1, text='Genero:', font=("Book Antiqua", 12, "bold"), bg= fondo_ventana, fg= 'black')
    texto_sexo.pack()
    texto_sexo.place(x=50, y=50)
    texto_sexo2 = tk.Label(ventana1, text='', font=("Book Antiqua", 12, "bold"), bg=fondo_entrada, fg="Black", relief='flat', width=12)
    texto_sexo2.pack()
    texto_sexo2.place(x=150, y=50)
    texto_sexo2.config(text=sexo)

    texto_distancia = tk.Label(ventana1, text='Distancia:', font=("Book Antiqua", 12, "bold"), bg= fondo_ventana, fg= 'black')
    texto_distancia.pack()
    texto_distancia.place(x=50, y=95)

    texto_distancia2 = tk.Label(ventana1, text='', font=("Book Antiqua", 12, "bold"), bg=fondo_entrada, fg="Black", relief='flat', width=12)
    texto_distancia2.pack()
    texto_distancia2.place(x=150, y=95)
    texto_distancia2.config(text=distancia)

    categoria1 = tk.Label(ventana1, text='Categoria:', font=("Book Antiqua", 12, "bold"), bg= fondo_ventana, fg= 'black')
    categoria1.pack()
    categoria1.place(x=50, y=140)

    categoria2 = tk.Label(ventana1, text='', font=("Book Antiqua", 12, "bold"), bg=fondo_entrada, fg="Black", relief='flat', width=12)
    categoria2.pack()
    categoria2.place(x=150, y=140)
    categoria2.config(text=categoria) 

    entreno1 = tk.Label(ventana1, text='Dia entreno:', font=("Book Antiqua", 12, "bold"), bg= fondo_ventana, fg= 'black')
    entreno1.pack()
    entreno1.place(x=50, y=185)

    entreno2 = tk.Label(ventana1, text='', font=("Book Antiqua", 12, "bold"), bg=fondo_entrada, fg="Black", relief='flat', width=12)
    entreno2.pack()
    entreno2.place(x=150, y=185)
    entreno2.config(text=entreno) 

    pais1 = tk.Label(ventana1, text='pais:', font=("Book Antiqua", 12, "bold"), bg= fondo_ventana, fg= 'black')
    pais1.pack()
    pais1.place(x=50, y=230)

    pais2 = tk.Label(ventana1, text='', font=("Book Antiqua", 12, "bold"), bg=fondo_entrada, fg="Black", relief='flat', width=12)
    pais2.pack()
    pais2.place(x=150, y=230)
    pais2.config(text=pais) 







    
#Frame1
Frame1 = tk.Frame()
Frame1.pack()
Frame1.config(bg=fondo_frame)
Frame1.config(width="385", height="120")    

nom = tk.Label(Frame1, text="Nombre", font=("Book Antiqua", 12, "bold"), bg=fondo_frame, fg="white")
nom.pack()
#nom.grid(row=0,column=0) separa en indices la ubicacion 
nom.place(x=50, y=15)

entrada = tk.Entry(ventana, width=35, relief="flat")
entrada.place(x=140, y=17)

#Frame2
Frame2 = tk.Frame()
Frame2.pack()
Frame2.config(bg=fondo_entrada)
Frame2.config(width="385", height="90")    

sex = tk.Label(Frame2, text="Sexo", font=("Book Antiqua", 12, "bold"), bg=fondo_entrada, fg="white")
sex.pack()
sex.place(x=50, y=25)

hombre_boton = tk.Radiobutton(Frame2, text='Hombre', variable= sexboton, value= 'hombre')
hombre_boton.pack()
hombre_boton.place(x=100, y=25)
mujer_boton = tk.Radiobutton(Frame2, text='Mujer', variable= sexboton, value= 'mujer')
mujer_boton.pack()
mujer_boton.place(x=170, y=25)

#Frame3
Frame3 = tk.Frame()
Frame3.pack()
Frame3.config(bg=fondo_frame)
Frame3.config(width="385", height="90")    

dist = tk.Label(Frame3, text="Distancia", font=("Book Antiqua", 12, "bold"), bg=fondo_frame, fg="white")
dist.pack()
dist.place(x=50, y=35)

primero = tk.Radiobutton(Frame3, text='5 km', variable= disboton, value= '5 km')
primero.pack()
primero.place(x=141, y=35)
segundo = tk.Radiobutton(Frame3, text='12 km', variable= disboton, value= '12 km')
segundo.pack()
segundo.place(x=196, y=35)
tercero = tk.Radiobutton(Frame3, text='17 km', variable= disboton, value= '17 km')
tercero.pack()
tercero.place(x=257, y=35)
cuarto = tk.Radiobutton(Frame3, text='24 km', variable= disboton, value= '24 km')
cuarto.pack()
cuarto.place(x=318, y=35)

#Frame4
Frame4 = tk.Frame()
Frame4.pack()
Frame4.config(bg=fondo_entrada)
Frame4.config(width="385", height="90")
dist = tk.Label(Frame4, text="Deporte", font=("Book Antiqua", 12, "bold"), bg=fondo_entrada, fg="black")
dist.pack()
dist.place(x=50, y=22)
barra = tk.Scrollbar(Frame4)
barra.place(x=327, y=20)
catego = tk.Listbox(Frame4,height=2, yscrollcommand = barra.set)
catego.place(x=200, y=22)

for element in my_list: # adding elements to Listbox

    catego.insert(tk.END,element)

barra.config( command = catego.yview)

#Frame5
Frame5 = tk.Frame()
Frame5.pack()
Frame5.config(bg=fondo_frame)
Frame5.config(width="385", height="90")
di = tk.Label(Frame5, text="Distancia", font=("Book Antiqua", 12, "bold"), bg=fondo_frame, fg="white")
di.pack()
di.place(x=50, y=22)
barra2 = tk.Scrollbar(Frame5)
barra2.place(x=327, y=15)
Dentreno = tk.Listbox(Frame5,height=3, yscrollcommand = barra2.set)
Dentreno.place(x=200, y=15)

for element2 in my_list2: # adding elements to Listbox

    Dentreno.insert(tk.END,element2)

barra2.config( command = Dentreno.yview) 

#Frame6
Frame6 = tk.Frame()
Frame6.pack()
Frame6.config(bg=fondo_entrada)
Frame6.config(width="385", height="90")
pa = tk.Label(ventana, text="pais", font=("Book Antiqua", 12, "bold"), fg="black")
pa.pack()
pa.place(x=50, y=482)
drop = OptionMenu(Frame6,pais_boton,*my_list3)
drop.pack()

# Botones

boton1 = tk.Button(ventana, text="Enviar", width=7, relief="groove", font=("Book Antiqua", 12),
                   cursor="pirate", command=login)
boton1.place(x=260, y=520)
boton1.bind("<Return>", (lambda event: login()))



ventana.mainloop()