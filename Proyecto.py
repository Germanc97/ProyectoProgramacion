from tkinter import *

v = Tk()


#menu





def niveles():
      """
      """
      canvasi = Canvas(v, width = 1200, height = 700)   
      canvasi.focus_set()
      canvasi.pack()


canvasi = Canvas(v, width = 1200, height = 700,)   
canvasi.focus_set()
canvasi.pack()
menu = PhotoImage(file = './menuinicio.gif')
canvasi.create_image(630,350, image=menu)


button1 = Button( text = "Quit", command = niveles, width= 30).place(x=500,y=410)
v.mainloop()

