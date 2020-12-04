#!/usr/bin/python3

import sys


def check_password(password, lower, upper, letter):

	count = 0

	for ele in password:
		if letter == ele:
			count += 1

	if count >= lower and count <= upper:
		return True

	return False


def main():

	c = 0
	for line in sys.stdin:
		protocol = line.rstrip().split()
		bounds = protocol[0].split('-')
		lower_bound = int(bounds[0])
		upper_bound = int(bounds[1])
		letter = protocol[1][0]
		if check_password(protocol[2], lower_bound, upper_bound, letter):
			c += 1

	print(c)

if __name__ == '__main__':
	main()
