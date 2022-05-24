# Author JRI 5/22/22

# Imports
from string import ascii_uppercase


# Functions
def cipher(shift):
    x = ascii_uppercase
    y = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]
    return dict(zip(x, y))

def shift(line, dict_key):
    new_line = "" # empty variable for return statment
    for character in line: # for loop to translate correctly for every character
        if character == " ":
            new_line += " "
            continue
        elif character == "\n":
            new_line += "\n" # keeps indents
            continue
        elif character == "!" or character == "," or character == "'": # keeps punctuation
            new_line += character
            continue
        character = character.upper() # only uppercase
        new_line = new_line + dict_key[character] # edit empty variable
    return new_line

def encrypt_message(filename, dict_key):
    lst = [] # empty list for the for loop
    end = "" # empty variable for ending statement
    it = open(filename)
    with it as file:
        for line in file: # for loop using the other function to encrypt
            lst += shift(line,dict_key)
        for lines in lst: # for loop to edit ending variable
            end += lines
        file = open("new_file.txt","w")
        file.write(end) # writes in new_file.txt
        file.close()

# input statements and calling functions
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

key = cipher(shift_value)

encrypt_message(user_file, key)
