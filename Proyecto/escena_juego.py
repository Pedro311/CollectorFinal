#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
from herramienta import Herramienta
from ladrillo import Ladrillo
from puntaje import *


class EscenaJuego(pilas.escenas.Escena):
    '''Representa a la escena que se desarrolla en la ejecucion del juego'''

    def __init__(self):
        pilas.escenas.Escena.__init__(self)
        self.crear_escenario()
        self.crear_colisiones()
        pilas.eventos.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla)

    def crear_escenario(self):
        self.fondo = pilas.fondos.Fondo('Fondo/ladrillo.jpg')
        """Agregamos a Tito"""
        self.cooperativista =pilas.actores.Cooperativista()
        self.cooperativista.aprender(pilas.habilidades.SeMantieneEnPantalla)
        self.cooperativista.escala = 0.7
        self.cooperativista.radio_de_colision=25
        self.cooperativista.y=-209
        """Agregamos las herramientas"""
        self.herramienta=Herramienta()*4
        """Agregamos los ladrillos"""
        self.ladrillo=Ladrillo()*4
        """Agregamos puntaje"""
        self.puntaje=pilas.actores.Puntaje()
        self.puntaje.x=206
        self.puntaje.y=210
        self.texto=pilas.actores.Texto('Puntos:')
        self.texto.x=130
        self.color = pilas.colores.negro
        self.texto.y=210
        """Agregamos el temporizador"""
        self.temporizador=pilas.actores.Temporizador()
        def funcion_callback():
            pilas.avisar("El juego termino!")
            escena_menu.EscenaMenu()

        self.temporizador.ajustar(60, funcion_callback)
        self.temporizador.iniciar()
        self.temporizador.y= 210

        pilas.avisar(u'ESC para salir')
   
    def crear_colisiones(self):
        def cuando_colisionan_ladrillo(ladrillo,cooperativista):
            import random
            self.ladrillo.y=240
            xl=[300,250,200,0,-200,-250,-300]
            random.shuffle(xl)
            self.ladrillo.x = xl
            self.puntaje.aumentar(-1)
            
        def cuando_colisionan_herramienta(herramienta,cooperativista):
            import random
            self.herramienta.y=240
            xh=[300,250,200,0,-200,-250,-300]
            random.shuffle(xh)
            self.herramienta.x = xh
            self.puntaje.aumentar(1)
        
        pilas.escena_actual().colisiones.agregar(self.ladrillo, self.cooperativista, cuando_colisionan_ladrillo)
        pilas.escena_actual().colisiones.agregar(self.herramienta, self.cooperativista, cuando_colisionan_herramienta)
    def cuando_pulsa_tecla(self, *k, **kv):
        import escena_menu
        escena_menu.EscenaMenu()
