import pygame
import sys
WIDTH = 720
HEIGHT = 720
RES = 80
ROW = HEIGHT//RES
COL = WIDTH//RES


def draw(fr):
	global grid
	global WIDTH
	global HEIGHT
	global RES
	global COL
	global ROW
	pygame.init()
	window = pygame.display.set_mode((WIDTH,HEIGHT))
	fps = pygame.time.Clock()
	pygame.font.init()
	myfont = pygame.font.SysFont('Comic Sans MS', 50)
	fps.tick(fr)
	window.fill((200,200,200))
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				pygame.quit()
				sys.exit()
	for y in range(COL):
		y_t = 1
		if(y==2 or y==5):
			y_t = 7
		pygame.draw.line(window, (0,0,0), (0, (y+1)*80), (WIDTH, (y+1)*80),y_t)
		for x in range(ROW):
			x_t=1
			actual = None if grid[y][x] == 0 else grid[y][x]
			if(actual != None):
				textsurface = myfont.render('%d '%(actual), False, (0, 0, 0))
				window.blit(textsurface,(x*RES+30,y*RES+30))
			if(x==2 or x==5):
				x_t = 7
			pygame.draw.line(window, (0,0,0), ((x+1)*80, 0), ((x+1)*80, HEIGHT),x_t)
	pygame.display.flip()