"""Problem: one edit away strings
 Returns true if two strings are one edit away from being the sameself.
adding a character, deleting a character, editing a character.
solve in O(n).
"""

def is_one_away(s1, s2):
    return False






    # NOTE: The following input values will be used for testing your solution.
    is_one_away("abcde", "abcd")  # should return True
    is_one_away("abde", "abcde")  # should return True
    is_one_away("a", "a")  # should return True
    is_one_away("abcdef", "abqdef")  # should return True
    is_one_away("abcdef", "abccef")  # should return True
    is_one_away("abcdef", "abcde")  # should return True
    is_one_away("aaa", "abc")  # should return False
    is_one_away("abcde", "abc")  # should return False
    is_one_away("abc", "abcde")  # should return False
    is_one_away("abc", "bcc")  # should return False
