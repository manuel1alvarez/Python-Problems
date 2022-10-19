"""
Write function that reverses a list, preferably in place.
"""

list1 =[1,2,3,4,5,]
list2 =[1,2,3,4,5,6,7,8]
list3 =['d','f','a','w']

def reverse_basic(list):
  last = len(list) - 1 #last index
  rev_list = [None] * len(list)
  for i in range(len(list)):
    rev_list[i] = list[last-i]
  return rev_list

def reverse_inplace(list):
  last = len(list) - 1 #last index
  for i in range(int(len(list)/2)):    
    temp_front = list[i]
    list[i] = list[last-i]
    list[last-i] = temp_front
  return list
    
print(reverse_inplace(list1))
