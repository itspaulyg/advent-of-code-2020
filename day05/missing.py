#!/usr/bin/python3

import sys


def find_missing(seats):

	target = seats[0]

	for num in seats:
		if target != num:
			print(target)
			break
		target += 1


def main():

	seats = []
	for line in sys.stdin:
		seats.append(line.strip())

	find_missing(list(map(int, seats)))


if __name__ == '__main__':
	main()
