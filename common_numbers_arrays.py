"""Problem: Wrtie a function that returns the common elements (as an array) between
two SORTED arrays of integers (ascending order). Solution in O(n,m)  a.k.a  O(n or m)

Solution: Move along both arrays using two pointers. Starting at index 0, p1 = p2 = 0.
if elements are the same at the current pointers add the element to the result (continue).
If element at p1 is larger than that one at p2 then increment p2 (continue).
Conversely if element for p2 is larger than that one at p1 then increment p1 (continue).
This method takes advantage of the fact that both arrays are ascending.
"""

def common_elements_simple(list1, list2): # trivial solution
    result = []
    for itemOne in list1:
        for itemTwo in list2:
            if (itemOne == itemTwo):
                result.append(itemOne)
    return result


def common_elements(list1, list2): # efficient solution, 2 pointers.
    result = []
    p1=0; p2=0;
    while (p1< len(list1) and p2 <len(list2)):
        if ( list1[p1] == list2[p2]):
            result.append(list1[p1])
            p1 = p1+1; p2 = p2+1;
        elif ( list1[p1] > list2[p2]):
            p2 = p2+1;
        else:
            p1 = p1+1;

    return result





list_a1 = [1, 3, 4, 6, 7, 9]
list_a2 = [1, 2, 4, 5, 9, 10]

list_b1 = [1, 2, 9, 10, 11, 12]
list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]

list_c1 = [0, 1, 2, 3, 4, 5]
list_c2 = [6, 7, 8, 9, 10, 11]
# common_elements(list_b1, list_b2) should return [] (an empty list).

print(common_elements(list_a1, list_a2))
