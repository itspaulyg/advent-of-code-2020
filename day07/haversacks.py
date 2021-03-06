#!/usr/bin/python3

import re
import sys

# Constants

CONTAIN_RE = r'^(.*) bags contain\s(.*)$'
TARGETS_RE = r'(\d+) ([a-z]+ [a-z]+) bags*[,.]' 

# Functions

def parse_rules():
    rules = {}

    for line in sys.stdin:
        source, targets = re.findall(CONTAIN_RE, line.strip())[0]
        rules[source]   = {}
        for count, target in re.findall(TARGETS_RE, targets):
            rules[source][target] = int(count)

    return rules

def contains(rules, source, target, first=False):
    if source == target:
        return not first

    return any(contains(rules, neighbor, target) for neighbor in rules[source])

# Main Execution

def main():
    rules = parse_rules()
    count = sum(1 for source in rules if contains(rules, source, 'shiny gold', True))

    print(count)

if __name__ == '__main__':
    main()
