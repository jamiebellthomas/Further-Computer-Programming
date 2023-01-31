# This will contain string operations for Exercise 3

def string_split(string:str):
    """
    This function takes a string and returns a list of strings
    """
    return string.split()

def list_sort(list_of_strings:list):
    """
    This function takes a list of strings and returns a list of strings
    """
    return sorted(list_of_strings)

def first_word(string:str):
    """
    This function takes a string and returns a string
    """
    return string.split()[0]

def first_and_last_word(string:str):
    """
    This function takes a string and returns a string
    """
    list_of_strings = string.split()
    return list_of_strings[0] + " " + list_of_strings[-1]

def first_and_last_word_sorted(string:str):
    """
    This function takes a string and returns a string
    """
    list_of_strings = string.split()
    list_of_strings = sorted(list_of_strings)
    return list_of_strings[0] + " " + list_of_strings[-1]