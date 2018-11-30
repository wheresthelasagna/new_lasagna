import pygame as pg
#settings
TILESIZE = 32
TILEWIDTH = 20
TILEHEIGHT = 16
WIDTH = TILEWIDTH*TILESIZE #x 4:5
HEIGHT = TILEHEIGHT*TILESIZE #y
WINDOW_SIZE = (WIDTH,HEIGHT) #(x,y)

#colors R G B
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

pos = [0,0] #avatar position
pupper = pg.transform.scale(pg.image.load('pupper_bread.gif'),(TILESIZE,TILESIZE)) #create player avatar
#pupper_rect = pg.Rect(pos[0],pos[1],pupper.get_width(),pupper.get_height())
thor = pg.transform.scale(pg.image.load('thor.png'),(TILESIZE*3,TILESIZE*2)) # 1342x742 1.808625
thor_rect = pg.Rect(pos[0],pos[1],thor.get_width(),thor.get_height())
star1 = (0,HEIGHT - TILESIZE)
star2 = (0,HEIGHT - TILESIZE*2)
star3 = (0 + TILESIZE,HEIGHT - TILESIZE)
star4 = (0 + TILESIZE,HEIGHT - TILESIZE*2)
star = pg.image.load('star.png')
