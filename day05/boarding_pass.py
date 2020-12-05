#!/usr/bin/python3

import sys


def find_row(rows):

	index = 0
	start = 0
	end = 127

	while start <= end and index < len(rows):
		mid = int((start + end) / 2)
		if rows[index] == 'F':
			end = mid
		elif rows[index] == 'B':
			start = mid + 1

		index += 1

	return start 


def find_col(cols):

	index = 0
	start = 0
	end = 7

	while start <= end and index < len(cols):
		mid = int((start + end) / 2)
		if cols[index] == 'L':
			end = mid
		elif cols[index] == 'R':
			start = mid + 1

		index += 1

	return start

def main():

	for line in sys.stdin:
		binary = line.strip()
		rows = binary[:7]
		cols = binary[7:]
		row = find_row(rows)
		col = find_col(cols)
		print(row * 8 + col)

if __name__ == '__main__':
	main()
