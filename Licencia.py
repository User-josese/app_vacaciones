import sys
from tkinter import *
from Principal import Principal


class Licencia:
    def __init__(self):
        self.ventana =Tk()
        self.ventana.title('TERMINOS Y CONDICIONES')
        self.ventana.resizable(False, False)
        self.ventana.geometry('600x360+600+300')
        self.ventana.iconbitmap(r'C:\app_vacaciones\icon0.ico')

        self.fondo=PhotoImage(file=r'C:\app_vacaciones\coca-cola-l.png')
        Label(self.ventana, image=self.fondo).place(x=300, y=220)

        #labels
        self.label1=Label(self.ventana, text='TERMINOS Y CONDICIONES')
        self.label1.config(font=('Arial', 13, 'bold'))
        self.label1.place(x=180, y=10)

        self.texo_condiciones= Text(self.ventana, width=96, height=12)
        self.texo_condiciones.configure(font=('Arial', 8), bg='white', state=NORMAL)
        self.texo_condiciones.insert(INSERT,  '''       
    TÉRMINOS Y CONDICIONES"

    A.  PROHIBIDA SU VENTA O DISTRIBUCIÓN SIN AUTORIZACIÓN DE INFORMATICONFIG.
    B.  PROHIBIDA LA ALTERACIÓN DEL CÓDIGO FUENTE O DISEÑO DE LAS INTERFACES GRÁFICAS.
    C.  INFORMATICONFIG DE ERNESTO NO SE HACE RESPONSABLE DEL MAL USO DE ESTE SOFTWARE.

    LOS ACUERDOS LEGALES EXPUESTOS A CONTINUACION RIGEN EL USO QUE USTED HAGA DE ESTE SOFTWARE
    (INFORMATICONFIG), NO SE RESPONSABILIZA DEL USO QUE USTED"
    HAGA CON ESTE SOFTWARE Y SUS SERVICIOS. PARA ACEPTAR ESTOS TERMINOS HAGA CLIC EN (ACEPTO)"
    SI USTED NO ACEPTA ESTOS TERMINOS, HAGA CLIC EN (NO ACEPTO) Y NO UTILICE ESTE SOFTWARE."
         ''')
        self.texo_condiciones.place(x=10, y=40)
        self.texo_condiciones.config(state=DISABLED)

        self.acepto=IntVar()
        self.check_acepto=Checkbutton(self.ventana, text='Yo acepto', font=('Arial', 12, 'bold'),\
                                      command=self.aceptar)
        self.check_acepto.place(x=10, y=260)

        #botones
        self.continuar=Button(self.ventana, text='Acepto', font=('Arial', 11, 'bold'),\
                              width=7, height=2, bd=3, state=DISABLED, command=self.acceso)
        self.continuar.place(x=10, y=290)

        self.cancelar=Button(self.ventana, text='Cancelar', font=('Arial', 11, 'bold'),\
                             width=7, height=2, bd=3, command=self.cancelar)
        self.cancelar.place(x=100, y=290)


        self.ventana.mainloop()

    def aceptar(self):
        if (self.continuar['state']==DISABLED):
            self.continuar['state']=NORMAL
        else:
            self.continuar['state']=DISABLED

    def acceso(self):
        self.ventana.destroy()
        Principal()

    def cancelar(self):
        sys.exit()
























