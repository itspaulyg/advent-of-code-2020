#!/usr/bin/python3

import sys


def handle_ops(ops):

	accum = 0
	index = 0
	visited = set()
	for i in range(len(ops)):
		if index in visited:
			break
		visited.add(index)
		op = ops[index][0]
		if op == 'acc':
			if ops[index][1][0] == '+':
				accum += int(ops[index][1][1:])
			else:
				accum -= int(ops[index][1][1:])
			index += 1
		elif op == 'jmp':
			if ops[index][1][0] == '+':
				index += int(ops[index][1][1:])
			else:
				index -= int(ops[index][1][1:])
		else:
			index += 1

	return accum


def main():

	ops = []
	for line in sys.stdin:
		ops.append(line.strip().split())

	accum = handle_ops(ops)

	print(accum)


if __name__ == '__main__':
	main()
