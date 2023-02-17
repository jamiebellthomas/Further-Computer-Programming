#Exercise 1 is an extension of CW1 (just adding exceptions)
#Exercise 2: Write a function that calculates the nth root of a number x . The function should take
#two arguments: x and n , where x is the number you want to find the root of, and n
#is the degree of the root you want to find (e.g. for a square root, n would be 2). The
#function should raise a ValueError exception if either of the following conditions are met:
#x is negative.
#n is negative or zero.

def nth_root(x, n):
    """
    Calculates the nth root of a number x
    x: number to find the root of
    n: degree of the root
    returns: nth root of x
    """
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

    
#Exercise 3: Read in a list of grades from grades.txt and print out the average grade.
"""
def average_grade():
    file = open('grades.txt', 'r')
    grades = file.readlines()
    #remove the new line character
    grades = [grade.strip() for grade in grades]

    #convert each string in grades list to a list of integers using ord()
    grades = [[ord(char)-96 for char in grade] for grade in grades]
    # Remove all -64 values from all lists
    grades = [[char for char in grade if char != -64] for grade in grades]
    #Average each list
    grades = [sum(grade)/len(grade) for grade in grades]
    # Round it to nearest whole number
    grades = [round(grade) for grade in grades]
    # Convert each number to a letter
    grades = [chr(grade+96) for grade in grades]
    print(grades)
    file.close()

"""
# Now funcitonality has been established, let's write it as sub-functions with exceptions
def read_grades():
    """
    Reads in a list of grades from grades.txt and returns it as a list
    returns: list of grades
    """
    # Raise an exception if the file is not found
    try:
        file = open('grades.txt', 'r')
    except FileNotFoundError:
        raise FileNotFoundError('File not found')
    else:
        grades = file.readlines()
        file.close()

        return grades

def convert_grades(grades):
    """
    Converts a list of grades to a list of lists of integers
    grades: list of grades (strings)
    returns: list of lists of integers
    """
    #remove the new line character
    grades = [grade.strip() for grade in grades]

    #convert each string in grades list to a list of integers using ord()
    grades = [[ord(char.lower())-96 for char in grade] for grade in grades]
    

    # Remove all -64 values from all lists
    grades = [[char for char in grade if char != -64] for grade in grades]
    # Raise exception if any grade is not a letter
    for grade in grades:
        for char in grade:
            if char < 1 or char > 26:
                raise ValueError('Grades must be letters')
    return grades

def average_grades(grades):
    """
    Averages a list of grades
    grades: list of grades (lists of integers)
    returns: individual average grades (strings)
    """
    #Average each list
    try:
        grades = [sum(grade)/len(grade) for grade in grades]
    except ZeroDivisionError:
        print('Division by zero')
    else:
    # Round it to nearest whole number
        grades = [round(grade) for grade in grades]
    # Convert each number to a letter
        grades = [chr(grade+96) for grade in grades]
    return grades


def main():
    grades = read_grades()
    try:
        grades = convert_grades(grades)
    except ValueError as error:
        print(error)
    else:
        try:
            grades = average_grades(grades)
        except ZeroDivisionError:
            print('Division by zero')
        else:
            print(grades)


if __name__ == '__main__':
    main()

