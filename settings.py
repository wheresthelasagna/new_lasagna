import pygame as pg
#settings
WIDTH = 320 #x
HEIGHT = 400 #y 4-5
WINDOW_SIZE = (WIDTH,HEIGHT) #(x,y)

#colors R G B
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pos = [0,0] #avatar position
pupper = pg.transform.scale(pg.image.load('pupper_bread.gif'),(75,75)) #create player avatar
#pupper_rect = pg.Rect(pos[0],pos[1],pupper.get_width(),pupper.get_height()) 