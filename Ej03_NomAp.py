 # CBTIS 89
# Elizabeth Lara Acuña 
# 3°B Programa T.M
# Programa  que muestre dos cuadros de texto. Uno para nombre y otro para el apellido.
#  Agrega un botón con el texto Mostrar el Nombre. Al oprimirlo deberá aparecer El nombre y el apellido juntos.
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tunombre y apellido")
ventana.geometry("300x200")

# Etiqueta de texto
etiqueta = tk.Label(ventana, text="Nombre y Apellido:", font=("Arial", 12))
etiqueta.pack(pady=10)

# Cuadro de texto
entrada1 = tk.Entry(ventana, font=("Arial", 12))
entrada1.pack(pady=5)
entrada2 = tk.Entry(ventana, font=("Arial", 12))
entrada2.pack(pady=5)

# Botón que responde a un evento
def mostrar_texto():
    texto = entrada1.get()
    texto2=entrada2.get()
    etiqueta_resultado.config(text=f"Tu nombre es: {texto} {texto2}")


boton = tk.Button(ventana, text="Mostrar Nombre", command=mostrar_texto)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)

# Iniciar el loop principal
ventana.mainloop()
