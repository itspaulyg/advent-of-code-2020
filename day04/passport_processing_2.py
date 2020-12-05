#!/usr/bin/python3

import sys


EYE_COLOR = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

def process_passport(passport):

	fields = set()
	data = []
	for i in range(len(passport)):
		for entry in passport[i]:
			fields.add(entry[:3])
			data.append(entry)

	return fields, data

def validate_passport(passport):

	for entry in passport:
		if entry[:3] == 'byr':
			byr = int(entry[4:])
			if byr > 2002 or byr < 1920:
				return False
		if entry[:3] == 'iyr':
			iyr = int(entry[4:])
			if iyr > 2020 or iyr < 2010:
				return False
		if entry[:3] == 'eyr':
			eyr = int(entry[4:])
			if eyr > 2030 or eyr < 2020:
				return False
		if entry[:3] == 'hgt':
			hgt = entry[4:]
			if hgt[-2:] == 'in':
				if int(hgt[:-2]) < 59 or int(hgt[:-2]) > 76:
					return False
			elif hgt[-2:] == 'cm':
				if int(hgt[:-2]) < 150 or int(hgt[:-2]) > 193:
					return False
			else:
				return False
		if entry[:3] == 'hcl':
			hcl = entry[4:]
			if hcl[0] != '#' and len(hcl) != 7:
				return False
		if entry[:3] == 'ecl':
			ecl = entry[4:]
			if ecl not in EYE_COLOR:
				return False
		if entry[:3] == 'pid':
			pid = entry[4:]
			if len(pid) != 9:
				return False

	return True


def main():

	passport = []
	valid = 0
	for line in sys.stdin:
		if line == '\n':
			fields, passport = process_passport(passport)
			if len(fields) == 7:
				if 'cid' not in fields:
					check = validate_passport(passport)
					if check: valid += 1
			elif len(fields) > 7:
				check = validate_passport(passport)
				if check: valid += 1
			passport = []
			continue
		passport.append(line.strip().split())

	print(valid)

if __name__ == '__main__':
	main()
