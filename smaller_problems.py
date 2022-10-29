"""
Just smaller problems that don't warrant their own file.
"""

"""swap two numbers without using a third value (in place)"""
def swap(a,b):
    a = a + b
    b = (b - a)*(-1) #(b - (a+b))*-1 --> (-a + (b-b))*-1  --> a
    a = a - b #((a+b)-a) --> (a-a) + b --> b
    return a, b




print(swap(100,-500))
print(swap(-1,-6))
