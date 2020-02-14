import numpy as np
import drawer

def ispossible(y,x,n):
	global grid;
	for y_axis in range(9):
		if grid[y_axis][x] == n:
			return False
	for x_axis in range(9):
		if(grid[y][x_axis] == n):
			return False
	for i in range(0,3):
		for j in range(0,3):
			if grid[(y//3)*3+i][(x//3)*3+j] == n:
				return False
	return True

def solve():
	global grid
	for j in range(9):
		for i in range(9):
			if grid[j][i] == 0:
				for n in range(1,10):
					if ispossible(j,i,n):
						grid[j][i] = n
						drawer.draw(600)
						solve()
						grid[j][i] = 0
				return
	print(np.matrix(grid))
	input("Another solution?")
