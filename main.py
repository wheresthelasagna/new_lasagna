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
move_up = False
move_down = False
orient = 'right'

while True: #game loop
	screen.fill(BLACK)
	if orient == 'right':
		screen.blit(thor,pos)
	elif orient == 'left':
		screen.blit(pg.transform.flip(thor,True,False),pos)
	if move_right:
		pos[0] += 8
	if move_left:
		pos[0] -= 8
	if move_up:
		pos[1] -= 4
	if move_down:
		pos[1] += 4

	thor_rect.x = pos[0]
	thor_rect.y = pos[1]

	if thor_rect.x > WIDTH: #set wrap
		pos[0] = 0 - thor.get_width()
	if thor_rect.x + thor.get_width() < 0:
		pos[0] = WIDTH
	if thor_rect.y > HEIGHT:
		pos[1] = 0 - thor.get_height()
	if thor_rect.y + thor.get_height() < 0:
		pos[1] = HEIGHT

	if thor_rect.colliderect(temp_rect):
		pg.draw.rect(screen,RED,temp_rect)
	else:
		pg.draw.rect(screen,GREEN,temp_rect)

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
				orient = 'right'
			if event.key == K_LEFT:
				move_left = True
				orient = 'left'
			if event.key == K_UP:
				move_up = True
			if event.key == K_DOWN:
				move_down = True
			if event.key == K_q:
				pg.quit()
				sys.exit()
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				move_right = False
			if event.key == K_LEFT:
				move_left = False
			if event.key == K_UP:
				move_up = False
			if event.key == K_DOWN:
				move_down = False

	pg.display.flip() #update display
	pg.time.Clock().tick(60) #maintain 60 fps
