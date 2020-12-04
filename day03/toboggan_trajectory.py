#!/usr/bin/python3

import sys


def walk_course(course):

	width = len(course[0])
	height = len(course)

	x = 0
	y = 0

	trees = 0

	while y < height:
		if course[y][x % width] == '#':
			trees += 1
		y += 1
		x += 3

	return trees

def main():

	course = []
	for line in sys.stdin:
		course.append(line.strip())

	print(walk_course(course))

if __name__ == '__main__':
	main()
