#!/usr/bin/python3

import sys


def evasive_manuever(action, move, ns, ew, wp_ns, wp_ew):

	if action == 'N':
		wp_ns += move
	elif action == 'S':
		wp_ns -= move
	elif action == 'E':
		wp_ew += move
	elif action == 'W':
		wp_ew -= move
	elif action == 'L':
		if move == 90:
			tmp = wp_ns
			wp_ns = wp_ew
			wp_ew = (-1) * tmp
		elif move == 180:
			wp_ns = (-1) * wp_ns
			wp_ew = (-1) * wp_ew
		elif move == 270:
			tmp = wp_ns
			wp_ns = (-1) * wp_ew
			wp_ew = tmp
	elif action == 'R':
		if move == 90:
			tmp = wp_ns
			wp_ns = (-1) * wp_ew
			wp_ew = tmp
		elif move == 180:
			wp_ns = (-1) * wp_ns
			wp_ew = (-1) * wp_ew
		elif move == 270:
			tmp = wp_ns
			wp_ns = wp_ew
			wp_ew = (-1) * tmp
	elif action == 'F':
		ns += move * wp_ns
		ew += move * wp_ew

	return ns, ew, wp_ns, wp_ew

def main():

	ns = 0
	ew = 0
	wp_ns = 1
	wp_ew = 10
	for line in sys.stdin:
		line = line.strip()
		action = line[0]
		move = int(line[1:])
		ns, ew, wp_ns, wp_ew = evasive_manuever(action, move, ns, ew, wp_ns, wp_ew)

	print(abs(ns) + abs(ew))

if __name__ == '__main__':
	main()
