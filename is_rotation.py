"""
Write a funciton that retrue true if one array is a rotation of another.
example: [1, 2, 3, 4, 5, 6, 7] and  [6, 7, 1, 2, 3, 4, 5]
No duplicates in these arrays.**

Solution: Find 2 indices where the arrays share a common element. Use these 2
indices loop through both arrays simultaneously and check for their similarity.
"""

def is_rotation(list1, list2):
    if len(list1) != len(list2): # different sizes, not a rotation.
        return False
    startIndex = -1;
    for x in range(0,len(list1)):
        if (list1[0] == list2[x]):
            startIndex = x # common element index for list2
            break
    if (startIndex == -1): # don't share the common element list1[0]
        return False

    for x in range(0,len(list1)):
        if ( startIndex == len(list1) ):
            startIndex = 0
        if (list1[x] != list2[startIndex]):
            return False
        startIndex = startIndex +1

    return True # doesn't fail any test, is a rotation.




list1 = [1, 2, 3, 4, 5, 6, 7]
list2a = [4, 5, 6, 7, 8, 1, 2, 3]
# is_rotation(list1, list2a) should return False.
list2b = [4, 5, 6, 7, 1, 2, 3]
# is_rotation(list1, list2b) should return True.
list2c = [4, 5, 6, 9, 1, 2, 3]
# is_rotation(list1, list2c) should return False.
list2d = [4, 6, 5, 7, 1, 2, 3]
# is_rotation(list1, list2d) should return False.
list2e = [4, 5, 6, 7, 0, 2, 3]
# is_rotation(list1, list2e) should return False.
list2f = [1, 2, 3, 4, 5, 6, 7]
# is_rotation(list1, list2f) should return True.
list2g = [6, 7, 1, 2, 3, 4, 5]

print( is_rotation(list1, list2g))
