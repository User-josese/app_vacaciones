import sys
from tkinter import *
from tkinter import ttk, messagebox


class Principal:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title('Pantalla principal')
        self.ventana.resizable(False, False)
        self.ventana.geometry('640x535+600+300')
        self.ventana.config(bg='red')
        self.ventana.iconbitmap(r'C:\app_vacaciones\icon0.ico')

        # barra de menu
        self.menubar1 = Menu(self.ventana)
        self.ventana.config(menu=self.menubar1)
        self.opciones1 = Menu(self.menubar1, tearoff=0)
        self.submenu1 = Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1)
        self.opciones1.add_command(label="Salir", command=self.salir,\
                                   font=('Arial', 10, 'bold'))

        # menú acerca de..
        self.opciones2 = Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label="Acerca de..", menu=self.opciones2, \
                                  font=('Arial', 10, 'bold'))
        self.opciones2.add_cascade(label="Info", command=self.acerca,\
                                   font=('Arial', 10, 'bold'))

        # diseño de fondo
        self.label1 = PhotoImage(file=r'C:\app_vacaciones\coca-cola-p.png')
        Label(self.ventana, image=self.label1, bg='red').place(x=0, y=0)

        # label Bienvenido
        self.labelbienvenida = Label(self.ventana, text='Bienvenid@!')
        self.labelbienvenida.config(fg='White', bg='red', font=('Andale Mono Regular', 20, 'bold'))
        self.labelbienvenida.place(x=340, y=30)

        # label datos
        self.labeldatos = Label(self.ventana, text='Datos del trabajador para el calculo de vacaciones')
        self.labeldatos.config(fg='White', bg='red', font=('Andale Mono Regular', 18))
        self.labeldatos.place(x=50, y=110)

        # label nombre completo
        self.l_nombre = Label(self.ventana, text='Nombre completo')
        self.l_nombre.config(fg='White', bg='red', font=('Andale Mono Regular', 11, 'bold'))
        self.l_nombre.place(x=30, y=160)

        # entry nombre completo
        self.datonombre = StringVar()
        self.e_nombre = Entry(self.ventana, bd=2, bg='#eee8e8', fg='red', textvariable=self.datonombre)
        self.e_nombre.config(font=('Andale Mono Regular', 12, 'bold'), width=22)
        self.e_nombre.place(x=30, y=185)

        # label apellido paterno
        self.l_amaterno = Label(self.ventana, text='Apellido paterno')
        self.l_amaterno.config(fg='White', bg='red', font=('Andale Mono Regular', 11, 'bold'))
        self.l_amaterno.place(x=30, y=225)

        # entry apellido paterno
        self.datoapa = StringVar()
        self.e_apaterno = Entry(self.ventana, bd=2, bg='#eee8e8', fg='red', textvariable=self.datoapa)
        self.e_apaterno.config(font=('Andale Mono Regular', 12, 'bold'), width=22)
        self.e_apaterno.place(x=30, y=250)

        # label apellido materno
        self.l_amaterno = Label(self.ventana, text='Apellido materno')
        self.l_amaterno.config(fg='White', bg='red', font=('Andale Mono Regular', 11, 'bold'))
        self.l_amaterno.place(x=30, y=295)

        # entry apellido materno
        self.datoama = StringVar()
        self.e_amaterno = Entry(self.ventana, bd=2, bg='#eee8e8', fg='red', textvariable=self.datoama)
        self.e_amaterno.config(font=('Andale Mono Regular', 12, 'bold'), width=22)
        self.e_amaterno.place(x=30, y=320)

        # label select departamento
        self.l_departamento = Label(self.ventana, text='Seleccione departamento')
        self.l_departamento.config(fg='White', bg='red', font=('Andale Mono Regular', 11, 'bold'))
        self.l_departamento.place(x=310, y=160)

        # combobox departamento
        self.var_combo1 = StringVar()
        self.opciones1 = (' ', 'Atención al Cliente', 'Departamento de Logística', 'Departamento de Gerencia')
        self.combobox1 = ttk.Combobox(self.ventana, state='readonly',
                                      width=20, font=('Andale Mono Regular', 11, 'bold'),
                                      textvariable=self.var_combo1,
                                      values=self.opciones1)
        self.combobox1.current(0)
        self.combobox1.place(x=310, y=185)

        # label select antiguedad
        self.l_antiguedad = Label(self.ventana, text='Seleccione la antiguedad')
        self.l_antiguedad.config(fg='White', bg='red', font=('Andale Mono Regular', 11, 'bold'))
        self.l_antiguedad.place(x=310, y=225)

        # combobox antiguedad
        self.var_combo2 = StringVar()
        self.opciones2 = (' ', '1 año de servicio', '2 a 6 años de servicio', '7 o mas años de servicio')
        self.combobox2 = ttk.Combobox(self.ventana, state='readonly',
                                      width=20, font=('Andale Mono Regular', 11, 'bold'),
                                      textvariable=self.var_combo2,
                                      values=self.opciones2)
        # estilo de los combobox
        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("TCombobox", fieldbackground="#EAEAEA", background="red")
        self.combobox2.current(0)
        self.combobox2.place(x=310, y=250)

        # label resultado
        self.l_resultado = Label(self.ventana, text='Resultado del cálculo')
        self.l_resultado.config(fg='White', bg='red', font=('Andale Mono Regular', 11, 'bold'))
        self.l_resultado.place(x=310, y=295)

        # textarea resultado
        self.area_resultado = Text(self.ventana, width=35, height=7)
        self.area_resultado.configure(font=('Andale Mono Regular', 11, 'bold'), \
                                      bg='#EAEAEA', fg='red', state=DISABLED)
        self.area_resultado.place(x=310, y=320)

        # label footer
        self.l_footer = Label(self.ventana, text='"©2017 The Coca-Cola Company | Todos los derechos reservados')
        self.l_footer.config(fg='White', bg='red', font=('Andale Mono Regular', 11, 'bold'))
        self.l_footer.place(x=85, y=480)

        self.botoncalcular = Button(self.ventana, text='Calcular', width=9, height=2, command=self.control_datos)
        self.botoncalcular.config(font=('Andale Mono Regular', 12, 'bold'), fg='White', bg='red', bd=5)
        self.botoncalcular.place(x=130, y=365)

        self.limpiar = Button(self.ventana, text='Limpiar', width=7, height=2, command=self.limpiadatos)
        self.limpiar.config(font=('Andale Mono Regular', 12, 'bold'), fg='White', bg='red', bd=5)
        self.limpiar.place(x=30, y=365)

        self.ventana.mainloop()

    def control_datos(self):
        if not self.datonombre.get() or not self.datoapa.get() or not self.datoama.get() \
                or self.var_combo1.get() == ' ' or self.var_combo2.get() == ' ':
            messagebox.showerror('AVISO', 'NO DEBEN QUEDAR CAMPOS VACIOS!')
        if len(self.datonombre.get()) > 10 or len(self.datoapa.get()) > 15 or len(self.datoama.get()) > 15:
            messagebox.showerror('AVISO', 'NOMBRE / APELLIDO(S) MUY LARGOS!')
        else:
            self.area_resultado.config(state=NORMAL)
            self.area_resultado.delete("1.0", "end")
            if self.var_combo1.get() == 'Atención al Cliente':
                if self.var_combo2.get() == '1 año de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + ' ' + self.datoama.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 14 DIAS DE VACACIONES')
                if self.var_combo2.get() == '2 a 6 años de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + ' ' + self.datoama.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 18 DIAS DE VACACIONES')
                if self.var_combo2.get() == '7 o mas años de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + ' ' + self.datoama.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 22 DIAS DE VACACIONES')
            if self.var_combo1.get() == 'Departamento de Logística':
                if self.var_combo2.get() == '1 año de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + ' ' + self.datoama.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 10 DIAS DE VACACIONES')
                if self.var_combo2.get() == '2 a 6 años de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + ' ' + self.datoama.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 15 DIAS DE VACACIONES')
                if self.var_combo2.get() == '7 o mas años de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + ' ' + self.datoama.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 20 DIAS DE VACACIONES')
            if self.var_combo1.get() == 'Departamento de Gerencia':
                if self.var_combo2.get() == '1 año de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + ' ' + self.datoama.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 18 DIAS DE VACACIONES')
                if self.var_combo2.get() == '2 a 6 años de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + ' ' + self.datoama.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 25 DIAS DE VACACIONES')
                if self.var_combo2.get() == '7 o mas años de servicio':
                    self.area_resultado.insert(INSERT,
                                               self.datonombre.get() + ' ' + self.datoapa.get() + ' ' + self.datoama.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antigüedad:' + self.var_combo2.get() + \
                                               '\n\n RECIBE 30 DIAS DE VACACIONES')
            self.area_resultado.config(state=DISABLED)

    def acerca(self):
        messagebox.showinfo('Info', '''        SISTEMA DE CONTROL DE VACACIONES
        Desarrollado por: INFORMATICONFIG©
        Derechos reservados 2022''')

    def salir(self):
        sys.exit()





    def limpiadatos(self):
        self.area_resultado.config(state=NORMAL)
        self.area_resultado.delete("1.0", "end")
        self.area_resultado.config(state=DISABLED)
        self.e_nombre.delete("0", "end")
        self.e_amaterno.delete("0", "end")
        self.e_apaterno.delete("0", "end")
        self.combobox2.current(0)
        self.combobox1.current(0)













