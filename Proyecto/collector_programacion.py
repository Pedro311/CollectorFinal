import pilas
import random
from pilas.escenas import Normal
from pilas.actores import Actor
pilas.iniciar()
fondo = pilas.actores.Actor('ppp.jpg')
fondo.escala=0.3
#Clase LADRILLO
class Ladrillo(Actor):
        def __init__(self, x=0,y=240):
            xLa=[300,200,0,-200,-300]
            imagen = pilas.imagenes.cargar('ladri.png')
            random.shuffle(xLa)
            Actor.__init__(self, imagen)
            self.rotacion = 2
            self.x = xLa
            self.y = y
            self.radio_de_colision = 30
            self.escala=0.2

        def actualizar(self):
            self.y=self.y-2
            if self.y == -220:
                self.y=240
            
#Clase HERRAMIENTA
class Herramienta(Actor):
        def __init__(self, x=0,y=240):
            xHe=[300,200,0,-200,-300]
            imagen = pilas.imagenes.cargar('LLave.png')
            random.shuffle(xHe)
            Actor.__init__(self, imagen)
            self.rotacion = 0
            self.x = xHe
            self.y = y
            self.radio_de_colision = 30
            self.escala=0.1

        def actualizar(self):
            self.y=self.y-2
            if self.y == -210:
                self.y=240
#Clase PASTO
class pasto(Actor):
    def __init__(self,x=0,y=0):
        imagen=pilas.imagenes.cargar("pasto.png")
        Actor.__init__(self,imagen)
        self.rotacion = 0
        self.x = x
        self.y = y
        self.radio_de_colision = 30
        self.escala=0.5

def iniciar_juego():
    pilas.escenas.Normal()
    pared = pilas.actores.Actor("ladrillo.jpg")
    plataforma = pasto()*15
    plataforma.y=-210
    plataforma[0].x=-260
    plataforma[1].x=-210
    plataforma[2].x=-160
    plataforma[3].x=-110
    plataforma[4].x=-60
    plataforma[5].x=-5
    plataforma[6].x=50
    plataforma[7].x=90
    plataforma[8].x=150
    plataforma[9].x=100
    plataforma[10].x=294
    plataforma[11].x=260
    plataforma[12].x=212
    plataforma[13].x=-293
    plataforma[14].x=170

    #tito
    c=pilas.actores.Cooperativista()
    d=pilas.actores.Dialogo()
    c.escala=0.8
    c.y=-209
    c.radio_de_colision=35
    c.centro=('centro','arriba')
    c.aprender(pilas.habilidades.SeMantieneEnPantalla)
    #Ladrillos
    ladrillo=Ladrillo()*3
    def choque_con_ladrillo(ladrillo,c):
        ladrillo.y=240
        pilas.avisar('CUIDADO CON LOS LADRILLOS!!')
        puntaje.aumentar(-1)
    pilas.escena_actual().colisiones.agregar(ladrillo,c,choque_con_ladrillo)
    puntaje = pilas.actores.Puntaje(x=206,y=210)
    #Herramientas
    herramientas=[Herramienta(),Herramienta(),Herramienta()]
    def choque_con_herramienta(herramientas,c):
        puntaje.aumentar(1)
        herramientas.y=240
        pilas.avisar('BIEN HECHO!!')

    pilas.escena_actual().colisiones.agregar(herramientas,c,choque_con_herramienta)
    #Puntaje

    texto = pilas.actores.Texto('Puntos:')
    texto.x = 130
    texto.y = 210


    #Temporizador
    t = pilas.actores.Temporizador()

    def funcion_callback():
        pilas.avisar("El juego termino!")
        escena_normal()

    t.ajustar(60, funcion_callback)
    t.iniciar()
    t.y= 210
    menu.eliminar()
    
def salir_del_juego():
    pilas.terminar()
    

menu = pilas.actores.Menu([('Jugar', iniciar_juego),
                    ('Salir', salir_del_juego)])


pilas.ejecutar()
