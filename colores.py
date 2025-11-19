 # CBTIS 89
# Elizabeth Lara Acuña 
# 3°B Programa T.M
import tkinter as tk 
from tkinter import ttk
#Creae ventana principal 
ventana=tk.Tk()
ventana.title("Lista desplegable ComboBox")
ventana.geometry("300x200")

#Etiqueta de instruccion
etiqueta=tk.Label(ventana,text="Elige una opcion:")
etiqueta.pack(pady=18)

#Crearlista desplegable (Combobox)
opciones=["Rojo","Verde","Azul","amarillo","Morado"]
ComboColores=ttk.Combobox(ventana,values=opciones,state="readonly")
ComboColores.pack(pady=5)

#Funcion que se ejecuta al seleccionar un elemento 
def mostrar_seleccion(event):
    seleccion=ComboColores.get()#Obtine el valor seleccionado 
    etiqueta_resultado.config(text=f"Seleccionaste:{seleccion}",fg="red")

#Asociar evento al seleccionarun elemento 
ComboColores.bind("<<ComboboxSelected>>",mostrar_seleccion)
    
#Etiqueta para mostrar el resultado 
etiqueta_resultado=tk.Label(ventana, text="Aun no has seleccionado nada")
etiqueta_resultado.pack(pady=20)
#Iniciar bucle principal 
ventana.mainloop()
