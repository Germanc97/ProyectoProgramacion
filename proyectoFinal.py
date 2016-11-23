from tkinter import *
import time
import random


#Este es el menu inicial de el juego donde se va apoder elegir si iniciar un juego nuevo o cargar uno anterior
v = Tk()
v.title("Sonic Bros")
canvas = Canvas(v, width = 1200, height = 700)
canvas.focus_set()
canvas.pack()
menu = PhotoImage(file="./menuinicio.gif")
canvas.create_image(630,350, image = menu)






class Niveles:

    def Nivel(self):
        """
        Esta funcion crea el menu donde se podra escoger los niveles.
        Entrada: Click en los botones
        Salida: Abre el nivel deseado
        """
        v.destroy()
        e = Tk()
        e.title("Niveles")
        self.canvas = Canvas(e, width = 1200, height = 700)
        self.canvas.pack()
        self.fondo = PhotoImage(file="./menuniveles.gif")
        self.canvas.create_image(600,350, image = self.fondo)
        self.b1 = Button(master = None, text = "Nivel 1", width= 30, height=1, command = niveles.Nivel1).place(x=460,y=210)
        self.e = e
        self.b2 = Button(master = None, text = "Nivel 2", width= 30, height=1, command = niveles.Nivel2).place(x=460,y=270)
        self.b3= Button(master = None, text = "Nivel 3", width= 30, height=1, command = niveles.Nivel3).place(x=460,y=340)
        self.b4 = Button(master = None, text = "Nivel 4", width= 30, height=1, command = niveles.Nivel4).place(x=460,y=410)
        self.b5 = Button(master = None, text = "Nivel 5", width= 30, height=1, command = niveles.Nivel5).place(x=460,y=480)

        
        
    def Mostrar1(self):
        """
        Esta funcion Muestra en pantalla el nombre digitado por el jugador 1.
        Entrada: Nombre digitado por el usuario
        Salida: Muestra en pantalla del nombre
        """

        self.nombre = self.Nombre1.get()
        self.lnombre = Label(self.f, text=self.nombre).place(x=20,y=10)
        self.f.mainloop()

    def Mostrar2(self):
        """
        Esta funcion Muestra en pantalla el nombre digitado por el jugador 2.
        Entrada: Nombre digitado por el usuario
        Salida: Muestra en pantalla del nombre
        """
        self.nombre = self.Nombre2.get()
        self.lnombre = Label(self.f, text=self.nombre).place(x=310,y=10)

    def puntaje1(self):
        """
        Esta funcion Muestra en pantalla el puntaje del jugador 1 y lo calcula.
        Entrada: Puntaje inicial.
        Salida: Muestra en pantalla el puntaje.
        """
        self.vida1 = 3
        self.puntaje1 = 0

        while self.vida1 > 3:
            self.puntaje1 = self.puntaje1 + 1
            time.sleep(0.1)
                   
        self.lpuntaje1 = Label(self.f, text="Puntaje: " + str(self.puntaje1)).place(x=130,y=10)

    def puntaje2(self):
        """
        Esta funcion Muestra en pantalla el puntaje del jugador 2 y lo calcula.
        Entrada: Puntaje inicial.
        Salida: Muestra en pantalla el puntaje.
        """
        self.vida2 = 3
        self.puntaje2 = 0

        while self.vida2 > 3:
            self.puntaje2 = self.puntaje2 + 1
            time.sleep(0.1)
                   
        self.lpuntaje2 = Label(self.f, text="Puntaje: " + str(self.puntaje2)).place(x=230,y=10)




    def vidas1(self):
        """
        Esta funcion Muestra en pantalla las vidas del jugador 1 y las calcula.
        Entrada: Vida inicial.
        Salida: Muestra en pantalla las vidas.
        """

        self.vida1 = 3

        if self.vida1 > 0:
            self.vida10 = True
        
        if self.puntaje1 == 100:
            self.vida1 == self.vida1 + 1
        elif self.puntaje1 == 200:
            self.vida1 == self.vida1 + 1
        elif self.puntaje1 == 300:
            self.vida1 == self.vida1 + 1
        elif self.puntaje1 == 400:
            self.vida1 == self.vida1 + 1
        elif self.puntaje1 == 500:
            self.vida1 == self.vida1 + 1
        elif self.puntaje1 == 600:
            self.vida1 == self.vida1 + 1

        self.lvidas1 = Label(self.f, text="Vidas: " + str(self.vida1)).place(x=390,y=287)
        


    def vidas2(self):
        """
        Esta funcion Muestra en pantalla las vidas del jugador 2 y las calcula.
        Entrada: Vida inicial.
        Salida: Muestra en pantalla las vidas.
        """
        self.vida2 = 3
        
        if self.puntaje2 == 100:
            self.vida2 == self.vida2 + 1
        elif self.puntaje2 == 200:
            self.vida2 == self.vida2 + 1
        elif self.puntaje2 == 300:
            self.vida2 == self.vida2 + 1
        elif self.puntaje2 == 400:
            self.vida2 == self.vida2 + 1
        elif self.puntaje2 == 500:
            self.vida2 == self.vida2 + 1
        elif self.puntaje2 == 600:
            self.vida2 == self.vida2 + 1

        self.lvidas2 = Label(self.f, text="Vidas: " + str(self.vida2)).place(x=390,y=319)



    def Nivel1(self):
        """
        Esta funcion crea el nivel 1, en cual se va a desarrollar el juego.
        Entrada: Los nombres de los jugadores y los personajes.
        Salida: Muestra en pantalla el juego.
        """

        self.e.destroy()
        f = Tk()
        f.title("Nivel 1")
        self.f = f
        self.canvas = Canvas(f, width = 450, height = 280)
        self.canvas.pack()
        self.fondo = PhotoImage(file="./Fondo.gif")
        self.canvas.create_image(230,140, image = self.fondo)
        
        self.sonic9 = PhotoImage(file="./Sonic.gif")
        self.sonic = self.canvas.create_image(210,238, image = self.sonic9)

        self.knuckles9 = PhotoImage(file="./Knuckles_Uppercut.gif")
        self.knuckles = self.canvas.create_image(260,237, image = self.knuckles9)
        self.Nombre1 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre1).pack()
        self.but1 = Button(self.f, text="OK", command = niveles.Mostrar1).place(x=330,y=285)
        self.Nombre2 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre2).pack()
        self.but2 = Button(self.f, text="OK", command = niveles.Mostrar2).place(x=330,y=313)
        self.digitenombre1 = Label(self.f, text="Nombre Jugador 1").place(x=5,y=287)
        self.digitenombre2 = Label(self.f, text="Nombre Jugador 2").place(x=5,y=317)
        niveles.puntaje1()
        niveles.puntaje2()
        niveles.vidas1()
        niveles.vidas2()
        niveles.enemigos1()

    def Nivel2(self):
        """
        Esta funcion crea el nivel 2, en cual se va a desarrollar el juego.
        Entrada: Los nombres de los jugadores y los personajes.
        Salida: Muestra en pantalla el juego.
        """
        self.e.destroy()
        f = Tk()
        f.title("Nivel 2")
        self.f = f
        self.canvas = Canvas(f, width = 450, height = 280)
        self.canvas.pack()
        self.fondo = PhotoImage(file="./Fondo.gif")
        self.canvas.create_image(230,140, image = self.fondo)
        
        self.sonic9 = PhotoImage(file="./Sonic.gif")
        self.sonic = self.canvas.create_image(210,238, image = self.sonic9)

        self.knuckles9 = PhotoImage(file="./Knuckles_Uppercut.gif")
        self.knuckles = self.canvas.create_image(260,237, image = self.knuckles9)
        self.Nombre1 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre1).pack()
        self.but1 = Button(self.f, text="OK", command = niveles.Mostrar1).place(x=330,y=285)
        self.Nombre2 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre2).pack()
        self.but2 = Button(self.f, text="OK", command = niveles.Mostrar2).place(x=330,y=313)
        self.digitenombre1 = Label(self.f, text="Nombre Jugador 1").place(x=5,y=287)
        self.digitenombre2 = Label(self.f, text="Nombre Jugador 2").place(x=5,y=317)
        niveles.puntaje1()
        niveles.puntaje2()
        niveles.vidas1()
        niveles.vidas2()
        niveles.enemigos2()

    def Nivel3(self):
        """
        Esta funcion crea el nivel 3, en cual se va a desarrollar el juego.
        Entrada: Los nombres de los jugadores y los personajes.
        Salida: Muestra en pantalla el juego.
        """
        self.e.destroy()
        f = Tk()
        f.title("Nivel 3")
        self.f = f
        self.canvas = Canvas(f, width = 450, height = 280)
        self.canvas.pack()
        self.fondo = PhotoImage(file="./Fondo.gif")
        self.canvas.create_image(230,140, image = self.fondo)
        
        self.sonic9 = PhotoImage(file="./Sonic.gif")
        self.sonic = self.canvas.create_image(210,238, image = self.sonic9)

        self.knuckles9 = PhotoImage(file="./Knuckles_Uppercut.gif")
        self.knuckles = self.canvas.create_image(260,237, image = self.knuckles9)
        self.Nombre1 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre1).pack()
        self.but1 = Button(self.f, text="OK", command = niveles.Mostrar1).place(x=330,y=285)
        self.Nombre2 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre2).pack()
        self.but2 = Button(self.f, text="OK", command = niveles.Mostrar2).place(x=330,y=313)
        self.digitenombre1 = Label(self.f, text="Nombre Jugador 1").place(x=5,y=287)
        self.digitenombre2 = Label(self.f, text="Nombre Jugador 2").place(x=5,y=317)
        niveles.puntaje1()
        niveles.puntaje2()
        niveles.vidas1()
        niveles.vidas2()
        niveles.enemigos3()

    def Nivel4(self):
        """
        Esta funcion crea el nivel 4, en cual se va a desarrollar el juego.
        Entrada: Los nombres de los jugadores y los personajes.
        Salida: Muestra en pantalla el juego.
        """
        self.e.destroy()
        f = Tk()
        f.title("Nivel 4")
        self.f = f
        self.canvas = Canvas(f, width = 450, height = 280)
        self.canvas.pack()
        self.fondo = PhotoImage(file="./Fondo.gif")
        self.canvas.create_image(230,140, image = self.fondo)
        
        self.sonic9 = PhotoImage(file="./Sonic.gif")
        self.sonic = self.canvas.create_image(210,238, image = self.sonic9)

        self.knuckles9 = PhotoImage(file="./Knuckles_Uppercut.gif")
        self.knuckles = self.canvas.create_image(260,237, image = self.knuckles9)
        self.Nombre1 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre1).pack()
        self.but1 = Button(self.f, text="OK", command = niveles.Mostrar1).place(x=330,y=285)
        self.Nombre2 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre2).pack()
        self.but2 = Button(self.f, text="OK", command = niveles.Mostrar2).place(x=330,y=313)
        self.digitenombre1 = Label(self.f, text="Nombre Jugador 1").place(x=5,y=287)
        self.digitenombre2 = Label(self.f, text="Nombre Jugador 2").place(x=5,y=317)
        niveles.puntaje1()
        niveles.puntaje2()
        niveles.vidas1()
        niveles.vidas2()
        niveles.enemigos4()

    def Nivel5(self):
        """
        Esta funcion crea el nivel 5, en cual se va a desarrollar el juego.
        Entrada: Los nombres de los jugadores y los personajes.
        Salida: Muestra en pantalla el juego.
        """
        self.e.destroy()
        f = Tk()
        f.title("Nivel 5")
        self.f = f
        self.canvas = Canvas(f, width = 450, height = 280)
        self.canvas.pack()
        self.fondo = PhotoImage(file="./Fondo.gif")
        self.canvas.create_image(230,140, image = self.fondo)
        
        self.sonic9 = PhotoImage(file="./Sonic.gif")
        self.sonic = self.canvas.create_image(210,238, image = self.sonic9)

        self.knuckles9 = PhotoImage(file="./Knuckles_Uppercut.gif")
        self.knuckles = self.canvas.create_image(260,237, image = self.knuckles9)
        self.Nombre1 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre1).pack()
        self.but1 = Button(self.f, text="OK", command = niveles.Mostrar1).place(x=330,y=285)
        self.Nombre2 = StringVar()
        self.entrada1 = Entry(self.f,textvariable=self.Nombre2).pack()
        self.but2 = Button(self.f, text="OK", command = niveles.Mostrar2).place(x=330,y=313)
        self.digitenombre1 = Label(self.f, text="Nombre Jugador 1").place(x=5,y=287)
        self.digitenombre2 = Label(self.f, text="Nombre Jugador 2").place(x=5,y=317)
        niveles.puntaje1()
        niveles.puntaje2()
        niveles.vidas1()
        niveles.vidas2()
        niveles.enemigos5()



    def enemigos1(self):
        """
        Esta funcion crea los enemigos de el nivel 1.
        Entrada: La imagen de el enemigo.
        Salida: Muestra los enemigos.
        """                                                            

        self.chaos9 = PhotoImage(file="./Chaos.gif")
        self.contador = 0
        while (self.contador < 1):
            self.x = random.randint(10,100)
            self.y = random.randint(10,100)
            self.chaos = self.canvas.create_image(40+self.x, 25+self.y, image = self.chaos9)
            self.contador = self.contador + 1
            
        
    def enemigos2(self):
        """
        Esta funcion crea los enemigos de el nivel 2.
        Entrada: La imagen de el enemigo.
        Salida: Muestra los enemigos.
        """ 
        self.chaos9 = PhotoImage(file="./Chaos.gif")
        self.contador = 0
        while (self.contador < 2):
            self.x = random.randint(10,100)
            self.y = random.randint(10,100)
            self.chaos = self.canvas.create_image(40+self.x, 25+self.y, image = self.chaos9)
            self.contador = self.contador + 1

    def enemigos3(self):
        """
        Esta funcion crea los enemigos de el nivel 3.
        Entrada: La imagen de el enemigo.
        Salida: Muestra los enemigos.
        """ 
        self.chaos9 = PhotoImage(file="./Chaos.gif")
        self.contador = 0
        while (self.contador < 3):
            self.x = random.randint(10,100)
            self.y = random.randint(10,100)
            self.chaos = self.canvas.create_image(40+self.x, 25+self.y, image = self.chaos9)
            self.contador = self.contador + 1

    def enemigos4(self):
        """
        Esta funcion crea los enemigos de el nivel 4.
        Entrada: La imagen de el enemigo.
        Salida: Muestra los enemigos.
        """ 
        self.chaos9 = PhotoImage(file="./Chaos.gif")
        self.contador = 0
        while (self.contador < 4):
            self.x = random.randint(10,100)
            self.y = random.randint(10,100)
            self.chaos = self.canvas.create_image(40+self.x, 25+self.y, image = self.chaos9)
            self.contador = self.contador + 1

  
    def enemigos5(self):
        """
        Esta funcion crea los enemigos de el nivel 5.
        Entrada: La imagen de el enemigo.
        Salida: Muestra los enemigos.
        """ 
        self.chaos9 = PhotoImage(file="./Chaos.gif")
        self.contador = 0
        while (self.contador < 5):
            self.x = random.randint(10,100)
            self.y = random.randint(10,100)
            self.chaos = self.canvas.create_image(40+self.x, 25+self.y, image = self.chaos9)
            self.contador = self.contador + 1
        



    

    




# Esta es la variable para hacer funcionar la clase y sus funciones.
niveles = Niveles()
# Este es el boton de el menu de inicio para abrir el menu de los niveles
buttniveles = Button(master = None, text = "Elegir Nivel", width= 30, height=1, command = niveles.Nivel).place(x=450,y=410)

