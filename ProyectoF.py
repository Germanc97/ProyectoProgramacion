from tkinter import *

v = Tk()
v.title("Sonic Bros")


#menu

canvasi = Canvas(v, width = 1200, height = 700,)   
canvasi.focus_set()
canvasi.pack()
menu = PhotoImage(file = './menuinicio.gif')
canvasi.create_image(630,350, image=menu)

      

def niveles():
      """
      """
      global v, canvasi, menu, menuniveles
      
      v.destroy()
      e = Tk()
      e.title("Niveles")
      canvasn = Canvas(e, width = 1200, height = 700)
      canvasn.pack()
      canvasn.focus_set()
      menuniveles = PhotoImage(file = './menuniveles.gif')
      canvasn.create_image(600,350, image = menuniveles)
      b1 = Button(master = None, text = "Nivel 1", width= 30, height=1, command = nivel1).place(x=460,y=210)
      b2 = Button(master = None, text = "Nivel 2", width= 30, height=1, command = niveles).place(x=460,y=310)
      b3 = Button(master = None, text = "Nivel 3", width= 30, height=1, command = niveles).place(x=460,y=410)
      b4 = Button(master = None, text = "Nivel 4", width= 30, height=1, command = niveles).place(x=460,y=510)
      b5 = Button(master = None, text = "Nivel 5", width= 30, height=1, command = niveles).place(x=460,y=610)
      return (e)
      e.mainloop()


def nivel1():
      """
      """
      global v, e, canvasi, menu, menuniveles, canvasn
      n1 = Tk()
      n1.title("Sonic Bros Nivel 1")
      canvasm = Canvas(n1, width = 1200, height = 700)
      canvasm.pack()
      canvasm.focus_set()
      sonic = PhotoImage(file = './Sonic.gif')
      canvasm.create_image(50,40, image=sonic)
      
      limit = False
      posx = 0
      posy = 0

      presionado = ["w","a","s","d"]

      
      def jump():
            """
            Procedimiento que realiza un salto
            Entrada: Ninguna
            Salida: El cuadrado salta en la ventana
            """
            global v, canvasm, posx, posy, limit, sonic, n1
            if (not limit):
                posy = posy - 10
            else:
                posy = posy + 10
            if (posy > -200 and not Limit):
                canvas.delete(sonic)
                sonic = canvasi.create_image(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,image=Sonic)
                n1.after(10, jump)
            else:
                Limit = True
                canvas.delete(sonic)
                sonic = canvasi.create_image(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,image=Sonic)
                if (posy != 0):
                    canvas.delete(sonic)
                    sonic = canvasi.create_image(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,image=Sonic)
                    n1.after(10, jump)


      def key(event):
          """
          Procedimiento que trata un evento del teclado

          """
          global v, canvasm, sonic, posx, posy, limit
          tecla = repr(event.char)
          print(tecla)
          if (tecla == "'a'"):
              posx = posx - 1
              canvas.delete(sonic)
              sonic = canvasi.create_image(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,image=Sonic)
          elif (tecla == "'d'"):
              posx = posx + 1
              canvas.delete(cuadrado)
              sonic = canvasi.create_image(200+posx,400+posy,200+posx,450+posy,250+posx,450+posy,250+posx,400+posy,image=Sonic)
          elif (tecla == "'w'"):
              limit = False
              jump()

    


      
bniveles = Button(master = None, text = "Elegir Nivel", width= 30, height=1, command = niveles).place(x=450,y=410)
v.mainloop()


