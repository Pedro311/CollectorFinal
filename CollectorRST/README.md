Collector
=========
¿ Que es colector?
-------------------------
Es un juego creado en Pilas-engine (version 0.68) sobre un ingeniero que debe recoger herramientas para sumar puntos , pero debe tener cuidado con los ladrillos que caigan. Estos le descontarán puntos.

¿Como se juega?
-----------------------
Utilizando las teclas de direccion debemos mover a Tito, el personaje de el juego, quien debera reunir la mayor cantidad de herramientas posibles, esquivando ladrillos.

Plataforma de Uso
----------------------------
Este juego corre en Python, dentro de la librera Pilas-Engine, especificamente la version 0.68 de Pilas-Engine.

Contacto
------------
Los desarrolladores de el juego, Agustin Marin y Juan Frattin, esperamos que si tienen sugerencias, dudas o cualquier consulta puenda consultarnos sin problemas.
  Aguus.marin@hotmail.com

Codigo de Juego
------------------------
.. code-block:: python
    :linenos:
    import pilas
    from pilas.escenas import Escena
	import escena_menu
	from pilas.actores import Actor
	import random
	from herramienta import Herramienta
	from ladrillo import Ladrillo
	from puntaje import *



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


	class Puntaje(pilas.actores.Puntaje):

		def __init__(self, x=206, y=210):
		    pilas.actores.Puntaje.__init__(self, x=x, y=y)
		    self.color = pilas.colores.negro
		    self.escala = 1.75
		    self.texto=pilas.actores.Texto('Puntos:')
		    self.texto.x=130
		    self.texto.y=210


	class Ladrillo(Actor):
		    def __init__(self, x=0,y=240):
		        import random
		        xLa=[300,250,200,0,-200,-250,-300]
		        imagen = pilas.imagenes.cargar('Personajes/ladri.png')
		        random.shuffle(xLa)
		        Actor.__init__(self, imagen)
		        self.rotacion = 0
		        self.x = xLa
		        self.y = y
		        self.radio_de_colision = 30
		        self.escala=0.1

		    def actualizar(self):
		        self.y=self.y-2
		        if self.y == -210:
		            self.y=240


	class Herramienta(Actor):
		    def __init__(self, x=0,y=240):
		        import random
		        xHe=[300,250,200,0,-200,-250,-300]
		        imagen = pilas.imagenes.cargar('Personajes/llave.png')
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
