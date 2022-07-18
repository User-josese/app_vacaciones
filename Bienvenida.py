from tkinter import *
from tkinter import messagebox
from Licencia import Licencia


class Bienvenida:
    def __init__(self):
        self.ventana=Tk()
        self.ventana.title('Acceso')
        self.ventana.resizable(False, False)
        self.ventana.geometry('350x450+800+300')
        self.ventana.configure(bg='red')


        self.fondo= PhotoImage(file=r'C:\app_vacaciones\logo-coca.png')
        Label(self.ventana, image=self.fondo, bg='red').pack()

        #Labels
        self.label1=Label(self.ventana, text='Sistema de control vacacional')
        self.label1.config(fg='White', bg='red', font=('Andale Mono Regular', 18, 'italic'))
        self.label1.place(x=10, y=140)
        self.label2=Label(self.ventana, text='Ingrese su nombre')
        self.label2.config(fg='White', bg='red', font=('Andale Mono Regular', 12, 'bold'))
        self.label2.place(x=50, y=230)
        self.label3=Label(self.ventana, text='©2022 The Coca-Cola Company.')
        self.label3.config(bg='red', fg='white', font=('Andale Mono Regular', 10, 'bold'))
        self.label3.place(x=70, y=410)


        #Entry nombre usuario
        self.dato1=StringVar()
        self.entry1=Entry(self.ventana, bd=2, bg='#eee8e8', fg='red', textvariable=self.dato1)
        self.entry1.config(font=('Andale Mono Regular', 12, 'bold'), width=27)
        self.entry1.place(x=50, y=255)

        #boton
        self.boton1= Button(self.ventana, text='Ingresar', bd=2, bg='White', fg='red')
        self.boton1.config(font=('Anda Mono Regular', 14), width=12, command=self.acceso)
        self.boton1.place(x=100, y=285)

        self.ventana.mainloop()

    def acceso(self):
        self.largo=self.dato1.get()
        if not self.dato1.get():
            messagebox.showerror('ATENCION', 'DEBE COLOCAR NOMBRE DE USUARIO!')
        elif len(self.largo)>0 and len(self.largo)<8:
            messagebox.showerror('ATENCION', 'EL NOMBRE DE USUARIO DEBE TENER MAS DE 8 CARACTERES')
        else:
            self.ventana.destroy()
            Licencia()

if __name__=='__main__':
    ejecutar=Bienvenida()













