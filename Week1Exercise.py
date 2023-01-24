#!/usr/bin/env python3
import sys
#Remove the first argument from the list of arguments
#This is the name of the script
sys.argv.pop(0)

if len(sys.argv) > 5:
    print("Too many arguments")
    exit()
    
sum = 0
for arg in sys.argv:
    sum += int(arg)
print(sum)