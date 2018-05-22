# Problem: Given an array find the most frequent item in O(n) time.
"""
Solution: Build a hashtable/dictionary containing the items in the array as keys
the values will represent the number of times the item occured in the array.
Next run a for loop through the hashtable and find the most occurent item and return it.

"""


def most_frequent(given_list):
    if (len(given_list) == 0):
        return None
    hashTable = {} # keys are the numbers, values are the number of occurences.
    for num in given_list:
        if num not in hashTable:
            hashTable[num]=1
        else:
            hashTable[num]= hashTable[num] + 1

    cur_max = None; prev_times = 0;
    for num in hashTable:
        cur_times = hashTable[num]
        if cur_times > prev_times:
            cur_max = num
            prev_times = cur_times

    return cur_max



list1 = [1, 3, 1, 3, 2, 1,3,3,3,3,3,3 ,6]
list2 = [3, 3, 1, 3, 2, 1]
list3 = []
list4 = [0]
list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]

print(most_frequent(list1))
print(most_frequent(list2))
print(most_frequent(list3))
print(most_frequent(list4))
print(most_frequent(list5))
