import pygame as pg
#settings
WIDTH = 720 #x
HEIGHT = 480 #y 4-5
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
thor = pg.transform.scale(pg.image.load('thor.png'),(181,100)) # 1342x742 1.808625
thor_rect = pg.Rect(pos[0],pos[1],thor.get_width(),thor.get_height())
temp_rect = pg.Rect(WIDTH/2,HEIGHT/2,pupper.get_width(),pupper.get_height())
