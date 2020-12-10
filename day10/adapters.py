#!/usr/bin/python3

import sys


ONE_JOLT = 0
THREE_JOLT = 0

def find_diff(adapters, num):

	global ONE_JOLT, THREE_JOLT

	if num == 1:
		ONE_JOLT += 1
		return

	if num - 1 == adapters[-1]:
		ONE_JOLT += 1
		find_diff(adapters[:-1], adapters[-1])
	elif num - 2 == adapters[-1]:
		find_diff(adapters[:-1], adapters[-1])
	elif num - 3 == adapters[-1]:
		THREE_JOLT += 1
		find_diff(adapters[:-1], adapters[-1])


def main():

	global ONE_JOLT, THREE_JOLT

	adapters = []
	for line in sys.stdin:
		adapters.append(int(line))

	adapters = sorted(adapters)
	find_diff(adapters[:-1], adapters[-1])

	print(ONE_JOLT)
	print(THREE_JOLT + 1)
	print(ONE_JOLT * (THREE_JOLT + 1))

if __name__ == '__main__':
	main()
