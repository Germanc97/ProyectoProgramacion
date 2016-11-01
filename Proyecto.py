from tkinter import *

v = Tk()


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
      canvasn = Canvas(e, width = 1200, height = 700)
      canvasn.pack()
      canvasn.focus_set()
      menuniveles = PhotoImage(file = './menuniveles.gif')
      canvasn.create_image(600,350, image = menuniveles)
      e.mainloop()
      
      
b1 = Button(master = None, text = "Elegir Nivel", width= 30, height=1, command = niveles).place(x=450,y=410)
v.mainloop()


