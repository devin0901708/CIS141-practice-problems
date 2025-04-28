'''
3. Prompt the user for a sentence and a word to try to find in that sentence.
Have the program print out whether the word was found in the sentence. (i.e. True or False)
'''
sentence = input("give a sentence you would like to find a word in. ")
word = input("What word would you like to find? ")
print(word in sentence)
