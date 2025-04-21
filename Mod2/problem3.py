'''
3. Create a program that prompts for the side lengths of a
triangle and computes the area using Heron's formula. 
(https://en.wikipedia.org/wiki/Heron%27s_formula) 
'''
a = float(input("what is the length of side 1?" ))
b = float(input("what is the length of side 2?" ))
c = float(input("what is the length of side 3?" ))
s = (0.5*(a+b+c))

semi = s*((s-a)*(s-b)*(s-c))

print (semi**(0.5))
