#!/usr/bin/python3

import sys


def process_passport(passport):

	fields = set()

	for i in range(len(passport)):
		for entry in passport[i]:
			fields.add(entry[:3])

	return fields

def main():

	passport = []
	valid = 0
	for line in sys.stdin:
		if line == '\n':
			print(passport)
			fields = process_passport(passport)
			if len(fields) == 7:
				if 'cid' not in fields:
					valid += 1
			elif len(fields) > 7:
				valid += 1
			print(fields)
			passport = []
			continue
		passport.append(line.strip().split())

	print(valid)

if __name__ == '__main__':
	main()
