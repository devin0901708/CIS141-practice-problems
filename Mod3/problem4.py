'''
4. Prompt the user for: a word, a first index, and a last index. 
Slice the word at the indexes provided by the user and print to the screen.
'''
word = input("Please give a word to slice. ")
first_index = int(input("Enter the first index. "))
end_index = int(input("Enter the ending index. "))
print(word[first_index:end_index])
