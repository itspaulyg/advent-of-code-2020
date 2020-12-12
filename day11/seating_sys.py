#!/usr/bin/python3

import sys

def check_seats(grid, spacer):

	change = False
	temp = grid.copy()
	grid = list()
	grid.append(spacer)
	for row in range(1, len(temp)-1):
		line = ','
		for col in range(1, len(temp[0])-1):
			seat = temp[row][col]
			if seat == '.':
				line += seat
				continue
			check = check_neighbors(seat, temp, row, col)
			if check:
				change = True
				if seat == 'L':
					line += '#'
				elif seat == '#':
					line += 'L'
			else:
				line += seat
		grid.append(line + ',')
	grid.append(spacer)
	return grid, change

def check_neighbors(seat, grid, row, col):

	check = 0
	if seat == 'L':
		if grid[row-1][col-1] == '#':
			check += 1
		if grid[row][col-1] == '#':
			check += 1
		if grid[row-1][col] == '#':
			check += 1
		if grid[row+1][col-1] == '#':
			check += 1
		if grid[row-1][col+1] == '#':
			check += 1
		if grid[row+1][col+1] == '#':
			check += 1
		if grid[row][col+1] == '#':
			check += 1
		if grid[row+1][col] == '#':
			check += 1
		if check:
			return False
	elif seat == '#':
		if grid[row-1][col-1] == '#':
			check += 1
		if grid[row][col-1] == '#':
			check += 1
		if grid[row-1][col] == '#':
			check += 1
		if grid[row+1][col-1] == '#':
			check += 1
		if grid[row-1][col+1] == '#':
			check += 1
		if grid[row+1][col+1] == '#':
			check += 1
		if grid[row][col+1] == '#':
			check += 1
		if grid[row+1][col] == '#':
			check += 1
		if check < 4:
			return False

	return True

def main():

	grid = []
	spacer = ''
	for _ in range(93):
		spacer += ','

	grid.append(spacer)
	for line in sys.stdin:
		grid.append(',' + line.strip() + ',')
	grid.append(spacer)

	change = True
	while change:
		grid, change = check_seats(grid, spacer)

	occupied = 0
	for line in grid:
		for elem in line:
			if elem == '#':
				occupied += 1

	print(occupied)

if __name__ == '__main__':
	main()
