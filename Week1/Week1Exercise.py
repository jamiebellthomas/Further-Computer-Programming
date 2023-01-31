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

#Usage of __name__ == "__main__"
#This is a way to test if a file is being run directly or if it is being imported
#If the file is being run directly, __name__ will be equal to __main__
#If the file is being imported, __name__ will be equal to the name of the file
#This is useful for testing if a file is being run directly or if it is being imported
#If the file is being run directly, you can run code that you want to run when the file is run directly
#If the file is being imported, you can run code that you want to run when the file is imported

# Simply:
if __name__ == "__main__":
    #Run code that you want to run when the file is run directly
    print("This is being run directly")
else:
    #Run code that you want to run when the file is imported
    print("This is being imported") 

