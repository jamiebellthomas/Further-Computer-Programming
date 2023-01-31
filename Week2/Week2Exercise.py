# Week 2 Exercise
# We're going to give up on shebangs and just use WSL command line rather than Bash
# This means we can use virtual environemnts and pip

def open_document(filename:str):
    """
    This function opens a file and returns the contents of the file
    """
    with open(filename,"r") as f:
        return f.read()

def convert_to_ints(string:str):
    """
    This function takes a string and returns a list of integers
    """
    list_of_strings = string.split()
    list_of_ints = []
    for string in list_of_strings:
        list_of_ints.append(int(string))
    return list_of_ints

def double_ints(list_of_ints:list):
    """
    This function takes a list of integers and returns a list of integers
    """
    doubled_list = []
    for integer in list_of_ints:
        doubled_list.append(integer*2)
    return doubled_list

def write_to_txt(filename:str,list_of_ints:list):
    """
    This function takes a list of integers and writes them to a file
    """
    with open(filename,"w") as f:
        for integer in list_of_ints:
            f.write(str(integer) + " ")

