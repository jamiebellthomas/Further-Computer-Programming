#!/usr/bin/env python3
import sys
print("This is the name of the script: ", sys.argv[0])
number_of_args = len(sys.argv)
print(number_of_args, "command line argument(s) inputted:")
for arg in sys.argv:
    print(arg)

