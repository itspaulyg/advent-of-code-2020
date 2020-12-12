#!/usr/bin/python3

import sys


def evasive_manuever(action, move, direction, ns, ew):

	if action == 'N':
		ns += move
	elif action == 'S':
		ns -= move
	elif action == 'E':
		ew += move
	elif action == 'W':
		ew -= move
	elif action == 'L':
		direction -= move
	elif action == 'R':
		direction += move
	elif action == 'F':
		curr_dir = abs(direction % 360)
		if curr_dir == 0:
			ns += move
		elif curr_dir == 90:
			ew += move
		elif curr_dir == 180:
			ns -= move
		elif curr_dir == 270:
			ew -= move

	return direction, ns, ew

def main():

	direction = 90
	ns = 0
	ew = 0
	for line in sys.stdin:
		line = line.strip()
		action = line[0]
		move = int(line[1:])
		direction, ns, ew = evasive_manuever(action, move, direction, ns, ew)

	print(abs(ns) + abs(ew))

if __name__ == '__main__':
	main()
