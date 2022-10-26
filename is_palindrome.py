"""
Write a Python Program to Check if a given sequence is a Palindrome or not?
Palindrome: a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""

"""
Solution 1: Given a sequence convert it to string. Loop through the sequence, at each index
compare the individual char to the one in its reverse form, if they are not equal return false. Otherwise,
if the whole sequence is traversed with no errors return true. This algorithm runs at O(n).
"""
def Palindrome(seq):
    seq = str(seq)
    last_index = len(seq) -1
    for i in range(len(seq)):
        if(seq[i] != seq[last_index-i]):
            return False
    return True


seq0 = ""; seq1 = 2332; seq2 = 22290007; seq3 = 151;
seq4 = "Radiohead"; seq5 = "dddd"; seq6 = "winners";
print(Palindrome(seq5))
