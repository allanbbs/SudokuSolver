import numpy as np
import math
import pygame
import sys
import solver
import drawer
import time
#############################################################
grid =  [					#################################
[4, 0, 0, 0, 0, 5, 0, 0, 0],#################################
[0, 0, 0, 0, 0, 0, 1, 0, 0],#################################
[3, 0, 0, 0, 8, 2, 4, 0, 0],#################################
[0, 0, 0, 1, 0, 0, 0, 8, 0],#################################
[9, 0, 3, 0, 0, 0, 0, 0, 0],#################################
[0, 0, 0, 0, 3, 0, 6, 7, 0],#################################
[0, 5, 0, 0, 0, 9, 0, 0, 0],#################################
[0, 0, 0, 2, 0, 0, 9, 0, 7],#####################################
[6, 4, 0, 3, 0, 0, 0, 0, 0]#####################################
]###############################################################
#################################################################
solver.grid = grid
drawer.grid = grid
'''def draw(fr):
	width = 720
	height = 720
	resolution = 80
	row = height//resolution
	col = width//resolution
	pygame.init()
	window = pygame.display.set_mode((width,height))
	fps = pygame.time.Clock()
	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', 50)
	w,z = 0,0
	fps.tick(fr)
	window.fill((200,200,200))
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()
	for y in range(col):
		y_t = 1
		if(y==2 or y==5):
			y_t = 7
		pygame.draw.line(window, (0,0,0), (0, (y+1)*80), (width, (y+1)*80),y_t)
		for x in range(row):
			x_t=1
			actual = None if grid[y][x] == 0 else grid[y][x]
			if(actual != None):
				textsurface = myfont.render('%d '%(actual), False, (0, 0, 0))
				window.blit(textsurface,(x*resolution+30,y*resolution+30))
			if(x==2 or x==5):
				x_t = 7
			pygame.draw.line(window, (0,0,0), ((x+1)*80, 0), ((x+1)*80, height),x_t)
	pygame.display.flip()'''
start = time.time()
solver.solve()
end = time.time()
print(end-start)
	






