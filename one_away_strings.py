"""Problem: one edit away strings
Given two strings s1,s2 the funcitons is_one_away() returns true if two strings are one edit away from being the same.
Possible edits adding a character, deleting a character, editing a character.
Solve in O(n) where n is the length of the string.

Solultion: First I make sure the strings are either the same size or differ by one.
If the strings are the same size, I make sure they are the same except at most one spot. Otherwise it is not one away.
If that doesn't come out as true, I next try the deleting a character method. I run a for loop along both strings wherever
they differ I delete that character. Then I check to see if s1 & s2 are now the same.
I run a similar process for the insert method. Although, if a one-away strings can be solved with the delete method it could
also be solved with the insert_method. So technically you only need one of the two methods.
This algorithm is O(n) because it loops through the n-sized strings only a few times (independent of size n).


"""

def is_one_away(s1, s2):
  if ( abs(len(s1)- len(s2)) > 1): # way different sizes, can't solve with one edit.
    return False
  # Swap s1,s2 so that s1 is shorter string.
  if (len(s1)> len(s2)):
    temp=s1; s1 = s2; s2 = temp;

  if (edit_method(s1,s2) or insert_method(s1,s2) or del_method(s1,s2) == True):
    return True
  else:
    return False

# equal size strings, maybe a single edit can make the strings equal.
def edit_method(s1,s2):
  if (len(s1) == len(s2)):
    num_errors = 0
    for i in range(0, len(s1)):
      if (s1[i] != s2[i]):
        num_errors +=1
      if (num_errors > 1):
        return False
  return True


def del_method(s1,s2):
  for i in range(0, len(s2)):
    if (len(s2) == i+1 ): # avoid going out of index in shorter string s1.
      s2 = s2[0:i] # delete at end.
      break
    if (s1[i] != s2[i]):
      s2 = s2[:i] + s2[(i+1):]
      break

  if (s1 == s2):
    return True
  else:
    return False


def insert_method(s1,s2):
  for i in range(0, len(s2)):
    if (len(s2) == i+1 ): # avoid going out of index in shorter string s1.
      s1 = s1 + s2[i] #insert at end.
      break
    if (s1[i] != s2[i]):
      s1 = s1[:i] + s2[i] + s1[i:] #insert
      break
  if (s1 == s2):
    return True
  else:
    return False









print is_one_away("abcd", "abc")  # should return True
print is_one_away("abcde", "abcd")  # should return True
print is_one_away("abde", "abcde")  # should return True
print is_one_away("a", "a")  # should return True
print is_one_away("abcdef", "abqdef")  # should return True
print is_one_away("abcdef", "abccef")  # should return True
print is_one_away("abcdef", "abcde")  # should return True
print is_one_away("aaa", "abc")  # should return False
print is_one_away("abcde", "abc")  # should return False
print is_one_away("abc", "abcde")  # should return False
print is_one_away("abc", "bcc")  # should return False
