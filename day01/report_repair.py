#!/usr/bin/python3

import sys


def sum_to_2020(base, nums):

	for num in nums:
		if num == base: continue 

		if (base + num) == 2020:
			return (num, base)
	return 0

def main():

	nums = []
	for line in sys.stdin:
		nums.append(line.rstrip())

	nums = list(map(int, nums))
	for num in nums:
		ans = sum_to_2020(num, nums)
		if ans: break

	print(ans[0]*ans[1])


if __name__ == '__main__':
	main()
