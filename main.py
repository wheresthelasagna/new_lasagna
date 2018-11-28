# http://usingpython.com/pygame-intro/
import pygame as pg
import sys
from pygame.locals import *
from settings import *

pg.init() #initiate pygame

pg.display.set_caption('things') #set title

screen = pg.display.set_mode(WINDOW_SIZE) #initiate the window

move_right = False
move_left = False

while True: #game loop
	screen.fill(BLACK)
	screen.blit(pupper,pos)
	pg.draw.rect(screen,BLUE,(WIDTH/2,HEIGHT/2,pupper.get_width(),pupper.get_height()))
	if move_right:
		pos[0] += 4
	if move_left:
		pos[0] -= 4
	for event in pg.event.get():
		if event.type == QUIT:
			pg.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_q:
				pg.quit()
				sys.exit()
			if event.key == K_RIGHT:
				move_right = True
			if event.key == K_LEFT:
				move_left = True
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				move_right = False
			if event.key == K_LEFT:
				move_left = False
	pg.display.flip() #update display
	pg.time.Clock().tick(60) #maintain 60 fps