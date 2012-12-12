#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
from pilas.escenas import Escena


class EscenaMenu(Escena):
    '''Representa a la escena que se desarrolla en el menu del juego'''

    def __init__(self):
        Escena.__init__(self)
        self.fondo = pilas.fondos.Fondo('Fondo/ppp.jpg')
        pilas.avisar('Use el teclado para cambiar o seleccionar opciones')
        self.generar_menu()

    def generar_menu(self):
        opciones = [
		            ('Jugar', self.comenzar),
		            ('Como Jugar', self.ayuda),
		            ('Salir', self.salir),
		           ]
        self.menu = pilas.actores.Menu(opciones)
        self.menu.color = pilas.colores.amarillo

    def comenzar(self):
        import escena_juego
        escena_juego.EscenaJuego()

    def ayuda(self):
        import escena_ayuda
        escena_ayuda.EscenaAyuda()

    def salir(self):
        pilas.terminar()
