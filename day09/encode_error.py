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


def main():

	preamble = []
	valid = True
	num = 0
	for line in sys.stdin:
		if len(preamble) == 25:
			valid, num = check_valid(list(map(int, preamble)), int(line))
			preamble = preamble[1:]
		if not valid:
			break
		preamble.append(line)

	print(num)

if __name__ == '__main__':
	main()
