#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pilas
import escena_menu


class Collector:
    '''Clase que llama a la escena menú para que comience el juego.'''
    
    def __init__(self):
        '''Inicia pilas con título "Collector", y gravedad 0.'''
        pilas.iniciar(titulo='Collector', gravedad=(0, 0))
        self.empezar()
        
    def empezar(self):
        '''Ejecuta la clase "Menu".'''
        escena_menu.EscenaMenu()
        pilas.ejecutar()
        

if __name__ == '__main__':
    Collector()
