#!/usr/bin/python3

import sys


def find_diff(adapters, num, cache):

	if num not in adapters:
		return 0

	if num == 5:
		return 2

	if num < 5:
		return 0

	if num not in cache:
		cache[num] = find_diff(adapters, num - 1, cache) + find_diff(adapters, num - 2, cache) + find_diff(adapters, num - 3, cache)

	return cache[num]


def main():

	adapters = []
	for line in sys.stdin:
		adapters.append(int(line))

	adapters = sorted(adapters)
	print(find_diff(adapters, adapters[-1], {}))


if __name__ == '__main__':
	main()
