import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import util.generic as utl
from forms.from_master import MasterPanel

class App:
    def __init__(self):
        self.ventana = tk.Tk()
        #modificar titulo
        self.ventana.title('Inicio de sesión')
        #dar valores
        self.ventana.geometry('800x500')
        #configuracion de fondo
        self.ventana.config(bg='#fcfcfc')
        #no permitir redimencionar
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)

        logo = utl.leer_imagen("./imagenes/logoEmpresa.png", (200, 200))

        #esto indica las configuraciones del frame y que ira colocado dentro de la ventana
        frame_logo   = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#FF3333')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#FF3333')
        label.place(x=0,y=0, relwidth=1, relheight=1)
        
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)
        
        #TITULO
        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top",fill=tk.X)
        title = tk.Label(frame_form_top, text="Inicio de sesión", font=('Time', 30), fg = "#666a88", bg="#fcfcfc", pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        #frame parte inferior
        frame_for_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_for_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        #usuario y contraseña
        #se crea la etiqueta usuario
        etq_user = tk.Label(frame_for_fill, text="Usuario", font=('Times', 14), fg ="#666a88", bg="#fcfcfc", anchor="w")
        etq_user.pack(fill=tk.X, padx=20, pady= 5)
        self.user = ttk.Entry(frame_for_fill, font=('Times', 14))
        self.user.pack(fill=tk.X, padx=20, pady=10)

        #se crea la etiqueta de la contraseña
        etq_pasw = tk.Label(frame_for_fill, text="Contraseña", font=('Times', 14), fg ="#666a88", bg="#fcfcfc", anchor="w")
        etq_pasw.pack(fill=tk.X, padx=20, pady= 5)
        self.pasw = ttk.Entry(frame_for_fill, font=('Times', 14))
        self.pasw.pack(fill=tk.X, padx=20, pady=10)
        self.pasw.config(show="*")




        self.ventana.mainloop()
