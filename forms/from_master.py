import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        #modificar titulo
        self.ventana.title('Maester panel')
        #modificar el ancho y alto
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        #dar valores
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        #configuracion de fondo
        self.ventana.config(bg='#fcfcfc')
        #no permitir redimencionar
        self.ventana.resizable(width=0, height=0)

        logo = utl.leer_imagen("./imagenes/logoEmpresa.png", (200, 200))

        label = tk.Label(self.ventana, image=logo, bg='#FF3333')
        label.place(x=0,y=0, relwidth=1, relheight=1)
        #la funcion de mainloop es mantener abierta la ventana 
        self.ventana.mainloop()