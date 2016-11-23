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
      b1 = Button(master = None, text = "Nivel 1", width= 30, height=1, command =nivel1).place(x=460,y=210)
      e.mainloop()
    



def nivel1():

      global fondo, sonic, e


      f = Tk()
      f.title("Sonic Bros Nivel 1")
      canvasn = Canvas(f, width = 1200, height = 700)
      canvasn.pack()
      canvasn.focus_set()
      Fondo0 = PhotoImage(file="Fondo.gif")
      fondo = Label(canvasn, image=Fondo0)
      fondo.place(x=100,y=100)
      fondo.pack()
      f.mainloop()








bniveles = Button(master = None, text = "Elegir Nivel", width= 30, height=1, command = niveles).place(x=450,y=410)
v.mainloop()




    
