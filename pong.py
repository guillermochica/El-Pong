#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Módulos
import pygame
from pygame.locals import *

# Constantes
#Anchura y altura de ventana
WIDTH = 640
HEIGHT = 480

# Clases
# Clase pelota
#Hereda métodos de pygame.sprite.Sprite
class Bola(pygame.sprite.Sprite):
	#Método que inicializa la clase
	def __init__(self):
		#Init de la clase heradada
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("images/ball.png", True) #True hace que se haga transparente
		self.rect = self.image.get_rect() #Obtiene un rectángulo con las dimensiones y posición de la imagen
		self.rect.centerx = WIDTH/2
		self.rect.centery = HEIGHT/2
		self.speed = [0.5,-0.5]
# ---------------------------------------------------------------------

# Funciones
#Cargar imagen
def load_image(filename, transparent=False): #filename: ruta del archivo

	try: image = pygame.image.load(filename)
	except pygame.error, message:
		raise SystemExit, message

	#Convierto la imagen al tipo interno de pygame
	image = image.convert()

	#Hacemos que la imagen sea transparente tomando como color le primer pixel
	if transparent:
		color = image.get_at((0,0))
		image.set_colorkey(color,RLEACCEL)

	return image

# ---------------------------------------------------------------------

def main():

	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	bola = Bola()

	pygame.display.set_caption("El Pong")

	background_image = load_image('images/fondo_pong.png')

	while True:
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)

		screen.blit(background_image, (0, 0))
		screen.blit(bola.image, bola.rect)
		pygame.display.flip()

	return 0

if __name__ == '__main__':

	pygame.init()

	main()
