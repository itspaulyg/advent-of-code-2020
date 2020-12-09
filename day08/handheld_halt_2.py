#!/usr/bin/python3

import sys


def handle_ops(ops):

	accum = 0
	index = 0
	visited = set()
	loop = False
	for i in range(len(ops)):
		if index in visited:
			loop = True
			break
		if index > len(ops):
			loop = True
			break
		if index == len(ops):
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

	return accum, loop


def change_op(ops):

	tmp = []
	for i in range(len(ops)):
		op = ops[i][0]
		tmp = ops.copy()
		if ops[i][0] == 'jmp':
			tmp[i][0] = 'nop'
		elif ops[i][0] == 'nop':
			tmp[i][0] = 'jmp'
		elif ops[i][0] == 'acc':
			continue
		accum, loop = handle_ops(tmp)
		if not loop:
			break
		ops[i][0] = op

	return accum


def main():

	ops = []
	for line in sys.stdin:
		ops.append(line.strip().split())

	accum = change_op(ops)

	print(accum)


if __name__ == '__main__':
	main()
