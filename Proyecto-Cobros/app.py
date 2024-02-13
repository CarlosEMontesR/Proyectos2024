from tkinter import *
from datetime import date
from FuncionesAgregarDeudor import *

def calcular_cobro():
    monto_prestamo = float(entrada_monto.get())
    tasa_interes = float(entrada_tasa.get())
    
    cobro_diario = monto_prestamo * (tasa_interes / 100) / 365
    cobro_semanal = cobro_diario * 7
    cobro_mensual = cobro_diario * 30
    
    hoy = date.today()
    fecha_vencimiento = hoy.strftime("%d/%m/%Y")
    
    texto_resultado.configure(text=f"Fecha de vencimiento: {fecha_vencimiento}\n\nCobro diario: {cobro_diario:.2f}\nCobro semanal: {cobro_semanal:.2f}\nCobro mensual: {cobro_mensual:.2f}")

# Crear ventana
ventana = Tk()
ventana.title("Interfaz de Préstamos")

# Etiquetas
Label(ventana, text="Monto del Préstamo:").grid(row=0, column=0, padx=5, pady=5)
Label(ventana, text="Tasa de Interés (%):").grid(row=1, column=0, padx=5, pady=5)
Label(ventana, text="Nombre del Cliente").grid(row=2, column=0, padx=5, pady=5)
# Entradas de texto
entrada_monto = Entry(ventana)
entrada_monto.grid(row=0, column=1, padx=5, pady=5)

entrada_tasa = Entry(ventana)
entrada_tasa.grid(row=1, column=1, padx=5, pady=5)

# Botón de calcular
boton_calcular = Button(ventana, text="Calcular", command=calcular_cobro)
boton_calcular.grid(row=2, column=0, columnspan=2, padx=5, pady=5)2


# Resultado
texto_resultado = Label(ventana, text="")
texto_resultado.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()
