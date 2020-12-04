#!/usr/bin/python3

import sys


def walk_course(course, dx, dy):

	width = len(course[0])
	height = len(course)

	x = 0
	y = 0

	trees = 0

	while y < height:
		if course[y][x % width] == '#':
			trees += 1
		y += dy
		x += dx

	return trees

def main():

	course = []
	for line in sys.stdin:
		course.append(line.strip())

	print(walk_course(course, 1, 1))
	print(walk_course(course, 3, 1))
	print(walk_course(course, 5, 1))
	print(walk_course(course, 7, 1))
	print(walk_course(course, 1, 2))

if __name__ == '__main__':
	main()
