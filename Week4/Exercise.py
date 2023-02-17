#Exercise 1 is an extension of CW1 (just adding exceptions)
#Exercise 2: Write a function that calculates the nth root of a number x . The function should take
#two arguments: x and n , where x is the number you want to find the root of, and n
#is the degree of the root you want to find (e.g. for a square root, n would be 2). The
#function should raise a ValueError exception if either of the following conditions are met:
#x is negative.
#n is negative or zero.

def nth_root(x, n):
    if x < 0:
        raise ValueError('x cannot be negative')
    if n <= 0:
        raise ValueError('n cannot be negative or zero')
    return x ** (1/n)

#print(nth_root(9, 2))
#print(nth_root(16, -2))
#print(nth_root(-16, 2))
test_cases = [(9, 2), (16, -2), (-16, 2)]
for case in test_cases:
    try:
        print(nth_root(case[0], case[1]))
    except ValueError as error:
        print(error)
    else:
        print('No exception raised')

    

