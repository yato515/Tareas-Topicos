    pais = tk.Label(ventana1, text='pais:', font=("Book Antiqua", 12, "bold"), bg= fondo_ventana, fg= 'black')
    pais.pack()
    pais.place(x=50, y=185)

    pais2 = tk.Label(ventana1, text='', font=("Book Antiqua", 12, "bold"), bg=fondo_entrada, fg="Black", relief='flat', width=12)
    pais2.pack()
    pais2.place(x=150, y=185)
    pais2.config(text=pais) 