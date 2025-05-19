'''
Construct a truth table for the expression:
(A AND B) OR (NOT B) where A and B each can be True or False. 
Your truth table should be commented out (as it's not valid Python code!)
'''
'''
A     B     A AND B     NOT B     Result
----------------------------------------
F     F     F           T         T
F     T     F           F         F
T     F     F           T         T
T     T     T           F         T
'''
combinations = [(False, False), (False, True), (True, False), (True, True)]

print("A     B     (A and B) or (not B)")
print("-------------------------------")
for A, B in combinations:
    result = (A and B) or (not B)
    print(f"{A}  {B}    {result}")
