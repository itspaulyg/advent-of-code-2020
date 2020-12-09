#!/usr/bin/python3

import sys


def check_valid(preamble, target):

	for num1 in preamble:
		for num2 in preamble:
			if num1 == num2:
				continue
			if (num1 + num2) == target:
				return True, 0

	return False, target


def find_weakness(preamble, target):

	tmp_set = []
	for num in preamble:
		if sum(tmp_set) > target:
			tmp_set = tmp_set[1:]
		if sum(tmp_set) == target:
			return tmp_set

		tmp_set.append(num)

	return []

def main():

	preamble = []
	valid = True
	num = 0
	target = 14360655
	for line in sys.stdin:
		if len(preamble) == 25:
			weakness_set = find_weakness(list(map(int, preamble)), target)
			if weakness_set:
				break
			preamble = preamble[1:]
		preamble.append(line)

	print(min(weakness_set) + max(weakness_set))

if __name__ == '__main__':
	main()
