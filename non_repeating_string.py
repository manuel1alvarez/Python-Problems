"""
Problem: Given a String finds the first character that is not repeated.

Solution: Build a hashtable/dictionary containing each char in the string as keys,
whereas the values will represent the number of times the char occured in the string.
Next, loop through the original string. Using the dictionary return the first string
that occurs once

"""


def non_repeating(given_string):
    if (len(given_string) == 0):
        return None
    char_dict = {} # keys are the numbers, values are the number of occurences.
    for char in given_string:
        if char not in char_dict:
            char_dict[char]=1
        else:
            char_dict[char]= char_dict[char] + 1

    for char in given_string:
        if (char_dict[char] == 1 ):
            return char
    return None






print(non_repeating("abcab")) # should return 'c'
non_repeating("abab") # should return None
non_repeating("aabbbc") # should return 'c'
non_repeating("aabbdbc") # should return 'd'
