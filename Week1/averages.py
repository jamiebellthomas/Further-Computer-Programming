#!/usr/bin/env python3
import sys
import statistics
import numpy as np
USAGE_MESSAGE = "Usage: ./averages.py {seperates numbers} [ARG]. Where [ARG]] is either --mean, --median or --mode [LIST OF NUMBERS CANNOT BE LONGER THAN 8]"
USAGE_MESSAGE2 = "e.g ./averages.py 1 2 3 --mean"
def print_usage():
    print(USAGE_MESSAGE)
    print(USAGE_MESSAGE2)
    quit()

def main(input:list):
    argument = sys.argv[-1]
    numbers = sys.argv[1:-1]
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    if len(sys.argv) > 8:
        print_usage()
        print("(Too many arguments)")
        quit()
    elif argument == "--mean":
        print(sum(numbers) / len(numbers))
        return sum(numbers) / len(numbers)
    elif argument == "--median":
        print(statistics.median(numbers))
        return statistics.median(numbers)
    elif argument == "--mode":
        print(statistics.mode(numbers))
        return statistics.mode(numbers)
    else:
        print_usage()
        
if __name__ == "__main__":
    main(sys.argv[1:])
