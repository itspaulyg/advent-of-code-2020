#!/usr/bin/python3

import sys


def count_questions(questions):

	count = 0
	seen = set()
	for elem in questions:
		for letter in elem:
			if letter not in seen:
				seen.add(letter)
				count += 1

	return count


def main():

	count = 0
	questions = []
	for line in sys.stdin:
		if line == '\n':
			count += count_questions(questions)
			questions = []
			continue

		questions.append(line.strip())

	print(count)

if __name__ == '__main__':
	main()
