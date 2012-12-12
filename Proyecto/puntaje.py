#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas


class Puntaje(pilas.actores.Puntaje):

    def __init__(self, x=206, y=210):
        pilas.actores.Puntaje.__init__(self, x=x, y=y)
        self.color = pilas.colores.negro
        self.escala = 1.75
        self.texto=pilas.actores.Texto('Puntos:')
        self.texto.x=130
        self.texto.y=210

