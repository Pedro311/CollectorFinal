#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
from pilas.escenas import Escena

class EscenaAyuda(Escena):
    '''Representa a la escena que se desarrolla en la ayuda del juego'''

    def __init__(self):
        Escena.__init__(self)
        self.fondo = pilas.fondos.Fondo('Fondo/fondo_ayuda.jpg')
        self.fondo.escala = 1.0
        pilas.eventos.pulsa_tecla_escape.conectar(self.cuando_pulsa_tecla)
        
    def cuando_pulsa_tecla(self, *k, **kv):
        import escena_menu
        escena_menu.EscenaMenu()
