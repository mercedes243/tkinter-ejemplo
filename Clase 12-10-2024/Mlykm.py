import tkinter as tk

def convertir():
    try:
        millas = float(entrada_millas.get())

        kilometros = millas * 1.60934

        etiqueta_resultado.config(text=f"{millas} millas son {kilometros} kilometros")
    except ValueError:
        etiqueta_resultado.config(text="Ingrese su valor numérico válido")

ventana = tk.Tk()
ventana.title("Conersor de Millas a Kilómetros")
ventana.geometry("300x150")

etiqueta_instruccion = tk.Label(ventana, text="Ingrese la distancia en millas:")
etiqueta_instruccion.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entrada_millas =tk.Entry(ventana)
entrada_millas.grid(row=1, column=1, padx=10, pady=10)

boton_convertir = tk.Button(ventana, text="Convertir", command=convertir)
boton_convertir.grid(row=1, padx=10, pady=10)

etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
ventana.mainloop()