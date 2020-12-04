#!/usr/bin/python3

import sys
import itertools

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
	for num in itertools.combinations(nums, 3):
		if num[0] + num[1] + num[2] == 2020:
			ans = num
			break

	print(ans[0]*ans[1]*ans[2])


if __name__ == '__main__':
	main()
