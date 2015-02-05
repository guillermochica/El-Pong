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
		self.speed = [0.5,-0.5] #speed[0]-> eje y

	# Actualizar
	def actualizar(self, time, pala_jug):
		#Actualiza la posición de la bola según la posición inicial
		#y el espacio (velocidad*tiempo) que recorre
		self.rect.centerx += self.speed[0]*time
		self.rect.centery += self.speed[1]*time

		#Para que la bola cambie de dirección al llegar a los extemos
		if self.rect.left <= 0 or self.rect.right >= WIDTH:
			self.speed[0] = -self.speed[0]
			self.rect.centerx += self.speed[0]*time

		if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
			self.speed[1] = -self.speed[1]
			self.rect.centery += self.speed[1]*time

		#comprobar colisiones
		if pygame.sprite.collide_rect(self, pala_jug):
			self.speed[0] = -self.speed[0] #si choca con pala cambiar dirección
			self.rect.centerx += self.speed[0]*time #actualizar posición

# Clase Pala
class Pala(pygame.sprite.Sprite):
	#Método que inicializa la clase
	def __init__(self,x):
		pygame.sprite.Sprite.__init__(self)
		self.image = load_image("images/pala.png")
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.centery = HEIGHT /2
		self.speed = 0.5

	def mover(self, time, keys):

		if self.rect.top >=0:
			if keys[K_UP]:
				self.rect.centery -=self.speed*time

		if self.rect.bottom <= HEIGHT:
			if keys[K_DOWN]:
				self.rect.centery += self.speed*time

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
	pala_jug = Pala(30)

	pygame.display.set_caption("El Pong")

	background_image = load_image('images/fondo_pong.png')

	clock = pygame.time.Clock()

	while True:
		time = clock.tick(60)
		keys = pygame.key.get_pressed()
		for eventos in pygame.event.get():
			if eventos.type == QUIT:
				sys.exit(0)

		bola.actualizar(time, pala_jug) #actualiza la posición de la bola
		pala_jug.mover(time,keys) #actualiza la posición de la pala
		screen.blit(background_image, (0, 0))
		screen.blit(bola.image, bola.rect)
		screen.blit(pala_jug.image, pala_jug.rect)
		pygame.display.flip()

	return 0

if __name__ == '__main__':

	pygame.init()

	main()
